"""Core agent with memory and evolution capabilities"""

import os
import ollama
import time
from typing import List, Dict, Any
from app.memory import MemoryManager, MemoryRetriever
from app.evolution import EvolutionEngine
from tools.functions import get_tools

class MemoryAgent:
    def __init__(self):
        # Use your existing llama3.2:1b model
        self.llm_model = "llama3.2:1b"
        self.memory_manager = MemoryManager()
        self.memory_retriever = MemoryRetriever()
        self.evolution_engine = EvolutionEngine()
        self.tools = get_tools()
        self.conversation_history = []
        
    def process_query(self, query: str, history: List[Dict] = None) -> Dict:
        """Process a user query and return response"""
        
        try:
            # Step 1: Retrieve relevant memories (with timeout)
            memories = self._retrieve_memories_with_timeout(query)
            
            # Step 2: Build context
            context = self._build_context(query, memories, history)
            
            # Step 3: Generate response (with timeout)
            response = self._generate_response_with_timeout(context)
            
            # Step 4: Save to memory (async)
            if response and not response.startswith("Error"):
                self.memory_manager.save(query, response)
            
            return {
                "response": response,
                "memories_used": memories,
                "context": context
            }
        except Exception as e:
            return {
                "response": f"Error: {str(e)}. Please try again.",
                "memories_used": [],
                "context": ""
            }
    
    def _retrieve_memories_with_timeout(self, query: str, timeout: int = 5) -> List:
        """Retrieve memories with timeout"""
        try:
            import threading
            result = []
            
            def retrieve():
                nonlocal result
                result = self.memory_retriever.retrieve(query, top_k=3)
            
            thread = threading.Thread(target=retrieve)
            thread.start()
            thread.join(timeout=timeout)
            
            if thread.is_alive():
                print("Memory retrieval timeout - using empty context")
                return []
            
            return result
        except:
            return []
    
    def _generate_response_with_timeout(self, context: str, timeout: int = 30) -> str:
        """Generate response with timeout"""
        try:
            prompt = f"""You are an intelligent assistant with memory.
            
Context:
{context}

Generate a helpful and accurate response based on the context.
If you don't know something, say so clearly.
Keep your response brief and to the point.
"""
            
            # Generate response with streaming to avoid timeout
            response = ollama.chat(
                model=self.llm_model,
                messages=[{"role": "user", "content": prompt}],
                options={
                    "num_predict": 256,  # Limit response length
                    "temperature": 0.7,
                    "top_k": 40,
                    "top_p": 0.9,
                }
            )
            
            return response['message']['content']
            
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def _build_context(self, query: str, memories: List, history: List) -> str:
        """Build context from query, memories, and history"""
        context = f"User Query: {query}\n\n"
        
        if memories:
            context += "Relevant Memories:\n"
            for mem in memories[:2]:  # Limit to 2 memories for speed
                context += f"- {mem.get('text', '')[:200]}\n"
        
        if history:
            context += "\nConversation History:\n"
            for msg in history[-2:]:  # Limit to last 2 messages
                context += f"{msg.get('role', '')}: {msg.get('content', '')[:100]}\n"
        
        return context
    
    def get_memory_stats(self) -> Dict:
        """Get memory statistics"""
        try:
            return self.memory_manager.get_stats()
        except:
            return {"total_memories": 0, "vector_count": 0}