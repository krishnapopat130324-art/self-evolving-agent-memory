"""Memory storage and retrieval system"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import chromadb
from chromadb.utils import embedding_functions
import os

class MemoryManager:
    def __init__(self):
        self.db_path = Path("data/memory.db")
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()
        
        # Initialize ChromaDB - with faster settings
        try:
            self.chroma_client = chromadb.PersistentClient(
                path="data/chroma_db",
                settings={
                    "anonymized_telemetry": False,
                    "allow_reset": True,
                }
            )
            
            # Use nomic-embed-text for embeddings
            self.embedding_fn = embedding_functions.OllamaEmbeddingFunction(
                model_name="nomic-embed-text",
                url="http://localhost:11434/api/embeddings"
            )
            
            # Get or create collection
            try:
                self.collection = self.chroma_client.get_collection("memories")
            except:
                self.collection = self.chroma_client.create_collection(
                    name="memories",
                    embedding_function=self.embedding_fn
                )
        except Exception as e:
            print(f"ChromaDB initialization error: {e}")
            self.collection = None
    
    def _init_db(self):
        """Initialize SQLite database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT,
                response TEXT,
                timestamp TEXT,
                metadata TEXT
            )
        """)
        conn.commit()
        conn.close()
    
    def save(self, query: str, response: str, metadata: dict = None):
        """Save memory to both SQLite and ChromaDB"""
        timestamp = datetime.now().isoformat()
        
        # Save to SQLite
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO memories (query, response, timestamp, metadata) VALUES (?, ?, ?, ?)",
            (query, response, timestamp, json.dumps(metadata or {}))
        )
        conn.commit()
        memory_id = cursor.lastrowid
        conn.close()
        
        # Save to ChromaDB for vector search (skip if not available)
        if self.collection:
            try:
                self.collection.add(
                    documents=[f"Query: {query}\nResponse: {response}"],
                    metadatas=[{"id": memory_id, "timestamp": timestamp}],
                    ids=[f"mem_{memory_id}"]
                )
            except Exception as e:
                print(f"ChromaDB save error: {e}")
        
        return memory_id
    
    def get_all(self) -> List[Dict]:
        """Get all memories from SQLite"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM memories ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        conn.close()
        
        memories = []
        for row in rows:
            memories.append({
                "id": row[0],
                "query": row[1],
                "response": row[2],
                "timestamp": row[3],
                "metadata": json.loads(row[4]) if row[4] else {}
            })
        return memories
    
    def get_stats(self) -> Dict:
        """Get memory statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM memories")
        count = cursor.fetchone()[0]
        conn.close()
        
        vector_count = 0
        if self.collection:
            try:
                vector_count = self.collection.count()
            except:
                vector_count = 0
        
        return {
            "total_memories": count,
            "vector_count": vector_count
        }


class MemoryRetriever:
    def __init__(self):
        self.db_path = Path("data/memory.db")
        try:
            self.chroma_client = chromadb.PersistentClient(
                path="data/chroma_db",
                settings={"anonymized_telemetry": False}
            )
            self.collection = self.chroma_client.get_collection("memories")
        except:
            self.collection = None
    
    def retrieve(self, query: str, top_k: int = 3) -> List[Dict]:
        """Retrieve relevant memories using vector search"""
        if not self.collection:
            return []
        
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=top_k
            )
            
            memories = []
            if results['ids']:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                for doc_id in results['ids'][0]:
                    if doc_id.startswith('mem_'):
                        memory_id = int(doc_id.split('_')[1])
                        cursor.execute(
                            "SELECT query, response, timestamp FROM memories WHERE id = ?",
                            (memory_id,)
                        )
                        row = cursor.fetchone()
                        if row:
                            memories.append({
                                "text": f"Query: {row[0]}\nResponse: {row[1]}",
                                "timestamp": row[2]
                            })
                conn.close()
            
            return memories
            
        except Exception as e:
            print(f"Retrieval error: {e}")
            return []