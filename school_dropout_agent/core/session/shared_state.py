"""
Shared state store for passing data between agents in a sequential workflow.
This is a simple in-memory store to hold agent results.
"""
from typing import Dict, Any, List

class SharedStateStore:
    _instance = None
    _results: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SharedStateStore, cls).__new__(cls)
            cls._instance._results = {}
        return cls._instance
    
    @classmethod
    def clear(cls):
        """Clear all stored results."""
        if cls._instance:
            cls._instance._results = {}
            
    @classmethod
    def save_result(cls, agent_name: str, result: Dict[str, Any]):
        """Save a result from an agent."""
        if cls._instance is None:
            cls()
        cls._instance._results[agent_name] = result
        
    @classmethod
    def get_all_results(cls) -> Dict[str, Any]:
        """Get all stored results."""
        if cls._instance is None:
            cls()
        return cls._instance._results.copy()
