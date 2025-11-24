"""
This module defines tools for the Risk Prediction Agent.
It mocks connections to SIS, LMS, and Financial systems to retrieve student data.
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta

# Mock data for demonstration
def get_student_attendance(student_id: str) -> Dict[str, Any]:
    """
    Fetches attendance records for a student.
    """
    # Mock logic: return low attendance for specific ID to test risk
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "total_classes": 40,
            "missed_classes": 10,
            "attendance_rate": 0.75,
            "recent_absences": 3, # Last 2 weeks
            "last_attended": (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        }
    return {
        "student_id": student_id,
        "total_classes": 40,
        "missed_classes": 2,
        "attendance_rate": 0.95,
        "recent_absences": 0,
        "last_attended": datetime.now().strftime("%Y-%m-%d")
    }

def get_student_grades(student_id: str) -> Dict[str, Any]:
    """
    Fetches current grades and assignment status.
    """
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "current_gpa": 2.1,
            "failed_courses": 1,
            "missing_assignments": 4,
            "recent_grades": [
                {"course": "Math 101", "grade": "D"},
                {"course": "History 202", "grade": "C-"}
            ]
        }
    return {
        "student_id": student_id,
        "current_gpa": 3.5,
        "failed_courses": 0,
        "missing_assignments": 0,
        "recent_grades": [
            {"course": "Math 101", "grade": "A"},
            {"course": "History 202", "grade": "B+"}
        ]
    }

def get_lms_activity(student_id: str) -> Dict[str, Any]:
    """
    Fetches Learning Management System (LMS) activity logs.
    """
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "last_login": (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d"),
            "average_daily_time_minutes": 5,
            "resources_viewed_last_week": 0
        }
    return {
        "student_id": student_id,
        "last_login": datetime.now().strftime("%Y-%m-%d"),
        "average_daily_time_minutes": 45,
        "resources_viewed_last_week": 12
    }

def get_financial_status(student_id: str) -> Dict[str, Any]:
    """
    Checks for financial holds or unpaid tuition.
    """
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "tuition_paid": False,
            "financial_hold": True,
            "outstanding_balance": 1500.00
        }
    return {
        "student_id": student_id,
        "tuition_paid": True,
        "financial_hold": False,
        "outstanding_balance": 0.0
    }
