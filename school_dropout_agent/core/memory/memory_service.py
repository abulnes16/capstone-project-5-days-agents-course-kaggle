"""
This module defines the MemoryService interface.
It specifies the contract for storing and retrieving student data, risk profiles, and interventions.
Implemented by concrete memory services (e.g., DatabaseMemoryService).
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime

class MemoryService(ABC):
    """Abstract interface for memory operations."""
    
    @abstractmethod
    def store_student_profile(self, student_id: str, profile_data: Dict[str, Any]) -> None:
        """Store or update a student's profile."""
        pass
    
    @abstractmethod
    def retrieve_student_history(self, student_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a student's complete history."""
        pass
    
    @abstractmethod
    def update_risk_profile(self, student_id: str, risk_data: Dict[str, Any]) -> None:
        """Update a student's risk assessment."""
        pass
    
    @abstractmethod
    def store_intervention(self, student_id: str, intervention_data: Dict[str, Any]) -> str:
        """Store an intervention and return its ID."""
        pass
    
    @abstractmethod
    def get_interventions(self, student_id: str) -> List[Dict[str, Any]]:
        """Get all interventions for a student."""
        pass
