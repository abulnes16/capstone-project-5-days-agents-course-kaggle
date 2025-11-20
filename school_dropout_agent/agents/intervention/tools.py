from typing import Dict, Any, List

def create_intervention(student_id: str, intervention_type: str, description: str) -> Dict[str, Any]:
    """
    Creates a new intervention record.
    """
    import uuid
    from datetime import datetime
    
    intervention_id = str(uuid.uuid4())
    return {
        "intervention_id": intervention_id,
        "student_id": student_id,
        "type": intervention_type,
        "status": "Pending",
        "description": description,
        "created_at": datetime.now().isoformat()
    }

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
