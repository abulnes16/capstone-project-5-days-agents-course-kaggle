from typing import Dict, Any, List
from school_dropout_agent.infrastructure.memory.database_memory import DatabaseMemoryService

# Initialize memory service
memory_service = DatabaseMemoryService()

def save_risk_assessment(student_id: str, risk_score: float, risk_level: str, risk_factors: List[str]) -> Dict[str, Any]:
    """
    Saves the risk assessment results to the database.
    Useful for sharing risk data with other agents and persisting history.
    """
    risk_data = {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "risk_factors": risk_factors
    }
    memory_service.update_risk_profile(student_id, risk_data)
    return {"status": "success", "message": f"Risk profile updated for {student_id}"}

def save_intervention_plan(student_id: str, interventions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Saves created interventions to the database.
    """
    created_ids = []
    for intervention in interventions:
        # Ensure type is string if it's an enum or other object
        if "type" in intervention and not isinstance(intervention["type"], str):
             intervention["type"] = str(intervention["type"])
             
        intervention_id = memory_service.store_intervention(student_id, intervention)
        created_ids.append(intervention_id)
        
    return {"status": "success", "created_intervention_ids": created_ids}

def get_student_context(student_id: str) -> Dict[str, Any]:
    """
    Retrieves the full student context (profile, risk, interventions) from the database.
    Useful for giving agents the full picture before they start their task.
    """
    history = memory_service.retrieve_student_history(student_id)
    if not history:
        return {"status": "not_found", "message": f"No history found for {student_id}"}
    return history
