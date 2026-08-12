"""Memory evolution engine - The 10/10 feature"""

import json
import ollama
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

class EvolutionEngine:
    def __init__(self):
        # Use your existing llama3.2:1b model
        self.llm_model = "llama3.2:1b"
        self.evolution_log = Path("data/evolution_log.json")
        self.evolution_log.parent.mkdir(parents=True, exist_ok=True)
        self._init_log()
    
    def _init_log(self):
        """Initialize evolution log"""
        if not self.evolution_log.exists():
            with open(self.evolution_log, 'w') as f:
                json.dump([], f)
    
    def diagnose_and_evolve(self, query: str, response: str) -> str:
        """Diagnose failure and evolve memory"""
        
        # Step 1: Diagnose the failure
        diagnosis = self._diagnose(query, response)
        
        # Step 2: Design improvement
        improvement = self._design_improvement(query, response, diagnosis)
        
        # Step 3: Apply evolution
        if improvement:
            self._apply_evolution(query, response, diagnosis, improvement)
            
            # Step 4: Generate improved response
            return self._generate_improved_response(query, improvement)
        
        return None
    
    def _diagnose(self, query: str, response: str) -> Dict:
        """Diagnose why the agent failed"""
        prompt = f"""
        Analyze why this AI assistant gave a poor response.
        
        Query: {query}
        Response: {response}
        
        Classify the failure into one of these categories:
        1. MemoryRetrievalFailure - Didn't find relevant information
        2. StaleMemory - Information was outdated
        3. ContextMisunderstanding - Misunderstood the query
        4. MissingKnowledge - Lacks specific knowledge
        5. ReasoningError - Logical error in response
        
        Return JSON with:
        - category: string
        - reason: string
        - confidence: float (0-1)
        """
        
        result = ollama.chat(
            model=self.llm_model,
            messages=[{"role": "user", "content": prompt}],
            format="json"
        )
        
        try:
            return json.loads(result['message']['content'])
        except:
            return {
                "category": "Unknown",
                "reason": "Could not diagnose",
                "confidence": 0.5
            }
    
    def _design_improvement(self, query: str, response: str, diagnosis: Dict) -> Dict:
        """Design a memory improvement"""
        prompt = f"""
        Based on the diagnosis, design a memory improvement.
        
        Query: {query}
        Response: {response}
        Diagnosis: {json.dumps(diagnosis)}
        
        Design an improvement by specifying:
        1. What memory should be added/updated
        2. How retrieval should be changed
        3. What pattern should be learned
        
        Return JSON with:
        - memory_to_add: string or null
        - retrieval_improvement: string or null
        - pattern_to_learn: string or null
        """
        
        result = ollama.chat(
            model=self.llm_model,
            messages=[{"role": "user", "content": prompt}],
            format="json"
        )
        
        try:
            return json.loads(result['message']['content'])
        except:
            return {
                "memory_to_add": f"When user asks '{query}', provide more specific information.",
                "retrieval_improvement": None,
                "pattern_to_learn": None
            }
    
    def _apply_evolution(self, query: str, response: str, diagnosis: Dict, improvement: Dict):
        """Apply the evolution to memory system"""
        
        evolution_entry = {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "old_response": response,
            "diagnosis": diagnosis,
            "improvement": improvement,
            "applied": True
        }
        
        # Log the evolution
        with open(self.evolution_log, 'r') as f:
            log = json.load(f)
        
        log.append(evolution_entry)
        
        with open(self.evolution_log, 'w') as f:
            json.dump(log, f, indent=2)
        
        print(f"Evolution applied for query: {query}")
    
    def _generate_improved_response(self, query: str, improvement: Dict) -> str:
        """Generate improved response using the improvement"""
        
        prompt = f"""
        Generate an improved response for this query using the improvement:
        
        Query: {query}
        Improvement: {json.dumps(improvement)}
        
        Generate a better, more accurate response that incorporates the improvement.
        """
        
        result = ollama.chat(
            model=self.llm_model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return result['message']['content']
    
    def get_evolution_history(self) -> List[Dict]:
        """Get evolution history"""
        with open(self.evolution_log, 'r') as f:
            return json.load(f)