"""
This module defines the Intervention entity.
It represents a specific action taken to support a student, such as tutoring or counseling.
Used by the InterventionCoordinatorAgent to create and track support actions.
"""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class InterventionStatus(Enum):
    PENDING = "Pending"
    ACTIVE = "Active"
    RESOLVED = "Resolved"
    CANCELLED = "Cancelled"

class InterventionType(Enum):
    ACADEMIC = "Academic"
    EMOTIONAL = "Emotional"
    FINANCIAL = "Financial"
    BEHAVIORAL = "Behavioral"
    FAMILY = "Family"

@dataclass
class Intervention:
    intervention_id: str
    student_id: str
    type: InterventionType
    status: InterventionStatus
    description: str
    created_at: datetime
    updated_at: datetime
    
    def mark_resolved(self):
        self.status = InterventionStatus.RESOLVED
        self.updated_at = datetime.now()
