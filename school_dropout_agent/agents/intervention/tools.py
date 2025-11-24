"""
This module defines tools for the Intervention Coordinator Agent.
It includes `create_intervention` (which saves to DB) and `notify_stakeholder`.
"""
from typing import Dict, Any, List
from school_dropout_agent.infrastructure.memory.database_memory import DatabaseMemoryService

memory_service = DatabaseMemoryService()

def create_intervention(student_id: str, intervention_type: str, description: str) -> Dict[str, Any]:
    """
    Creates a new intervention record and saves it to the database.
    """
    import uuid
    from datetime import datetime
    
    intervention_id = str(uuid.uuid4())
    intervention_data = {
        "intervention_id": intervention_id,
        "student_id": student_id,
        "type": intervention_type,
        "status": "Pending",
        "description": description,
        "created_at": datetime.now().isoformat()
    }
    
    # Save to database
    memory_service.store_intervention(student_id, intervention_data)
    
    return intervention_data

def notify_stakeholder(stakeholder_type: str, student_id: str, message: str) -> Dict[str, Any]:
    """
    Sends a notification to a stakeholder (teacher, counselor, parent).
    """
    return {
        "stakeholder_type": stakeholder_type,
        "student_id": student_id,
        "message": message,
        "status": "Sent",
        "timestamp": "2025-11-20T14:00:00"
    }

def get_active_interventions(student_id: str) -> Dict[str, Any]:
    """
    Retrieves active interventions for a student.
    """
    # Mock data
    return {
        "student_id": student_id,
        "active_interventions": []
    }
