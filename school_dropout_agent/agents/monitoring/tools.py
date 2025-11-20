from typing import Dict, Any
from datetime import datetime, timedelta

def get_intervention_outcome(intervention_id: str) -> Dict[str, Any]:
    """
    Retrieves the outcome of a specific intervention.
    """
    # Mock data
    return {
        "intervention_id": intervention_id,
        "status": "Completed",
        "outcome": "Improved",
        "notes": "Student attended tutoring sessions and grades improved."
    }

def compare_metrics(student_id: str, metric_type: str, before_date: str, after_date: str) -> Dict[str, Any]:
    """
    Compares student metrics before and after an intervention.
    """
    # Mock data
    if metric_type == "attendance":
        return {
            "student_id": student_id,
            "metric_type": metric_type,
            "before": 0.75,
            "after": 0.85,
            "improvement": 0.10,
            "improved": True
        }
    elif metric_type == "gpa":
        return {
            "student_id": student_id,
            "metric_type": metric_type,
            "before": 2.1,
            "after": 2.5,
            "improvement": 0.4,
            "improved": True
        }
    return {
        "student_id": student_id,
        "metric_type": metric_type,
        "before": None,
        "after": None,
        "improvement": 0,
        "improved": False
    }

def record_outcome(intervention_id: str, outcome: str, notes: str) -> Dict[str, Any]:
    """
    Records the outcome of an intervention.
    """
    return {
        "intervention_id": intervention_id,
        "outcome": outcome,
        "notes": notes,
        "recorded_at": datetime.now().isoformat()
    }
