"""
This module defines tools for the Monitoring Agent.
It provides functionality to check intervention status and recent academic progress.
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta
from school_dropout_agent.infrastructure.mock_data import MockDataStore

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

def compare_metrics(student_id: str) -> Dict[str, Any]:
    """
    Compares current metrics with historical data.
    """
    # Fetch current data from MockDataStore
    current_attendance = MockDataStore.get_student_data(student_id, "attendance")
    current_grades = MockDataStore.get_student_data(student_id, "grades")
    
    # Mock historical data (e.g., from last month)
    # In a real system, this would query the database for past records
    
    attendance_trend = "Stable"
    if current_attendance and current_attendance.get("attendance_rate", 1.0) < 0.8:
        attendance_trend = "Declining"
        
    grade_trend = "Stable"
    if current_grades and current_grades.get("failed_courses", 0) > 0:
        grade_trend = "Declining"

    return {
        "student_id": student_id,
        "attendance_trend": attendance_trend,
        "grade_trend": grade_trend,
        "notes": "Comparison based on mock historical baseline."
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
