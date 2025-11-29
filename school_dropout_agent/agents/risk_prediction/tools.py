"""
This module defines tools for the Risk Prediction Agent.
It mocks connections to SIS, LMS, and Financial systems to retrieve student data.
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta

from school_dropout_agent.infrastructure.mock_data import MockDataStore

# Mock data for demonstration
def get_student_attendance(student_id: str) -> Dict[str, Any]:
    """
    Fetches attendance records for a student.
    """
    data = MockDataStore.get_student_data(student_id, "attendance")
    if data:
        data["student_id"] = student_id
        return data
    
    # Fallback for unknown IDs
    return {
        "student_id": student_id,
        "total_classes": 40,
        "missed_classes": 0,
        "attendance_rate": 1.0,
        "recent_absences": 0,
        "last_attended": datetime.now().strftime("%Y-%m-%d")
    }

def get_student_grades(student_id: str) -> Dict[str, Any]:
    """
    Fetches current grades and assignment status.
    """
    data = MockDataStore.get_student_data(student_id, "grades")
    if data:
        data["student_id"] = student_id
        return data

    return {
        "student_id": student_id,
        "current_gpa": 3.0,
        "failed_courses": 0,
        "missing_assignments": 0,
        "recent_grades": []
    }

def get_lms_activity(student_id: str) -> Dict[str, Any]:
    """
    Fetches Learning Management System (LMS) activity logs.
    """
    data = MockDataStore.get_student_data(student_id, "lms")
    if data:
        data["student_id"] = student_id
        return data

    return {
        "student_id": student_id,
        "last_login": datetime.now().strftime("%Y-%m-%d"),
        "average_daily_time_minutes": 30,
        "resources_viewed_last_week": 5
    }

def get_financial_status(student_id: str) -> Dict[str, Any]:
    """
    Checks for financial holds or unpaid tuition.
    """
    data = MockDataStore.get_student_data(student_id, "financial")
    if data:
        data["student_id"] = student_id
        return data

    return {
        "student_id": student_id,
        "tuition_paid": True,
        "financial_hold": False,
        "outstanding_balance": 0.0
    }
