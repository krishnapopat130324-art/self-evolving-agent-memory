"""Unit tests for the system"""

import unittest
import json
from pathlib import Path
from app.memory import MemoryManager, MemoryRetriever
from app.evolution import EvolutionEngine

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory_manager = MemoryManager()
        
    def test_save_memory(self):
        result = self.memory_manager.save("Test query", "Test response")
        self.assertIsNotNone(result)
    
    def test_get_all(self):
        memories = self.memory_manager.get_all()
        self.assertIsInstance(memories, list)

class TestEvolution(unittest.TestCase):
    def setUp(self):
        self.evolution = EvolutionEngine()
    
    def test_diagnose(self):
        diagnosis = self.evolution._diagnose("What is Python?", "I don't know")
        self.assertIn("category", diagnosis)

if __name__ == "__main__":
    unittest.main()