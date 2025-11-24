"""
This module defines tools for the Emotional & Behavioral Agent.
It mocks retrieval of counseling logs and student survey responses.
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta

def get_counseling_visits(student_id: str) -> Dict[str, Any]:
    """
    Fetches counseling visit records for a student.
    """
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "total_visits": 5,
            "recent_visits": 3,  # Last 30 days
            "last_visit_date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
            "reported_issues": ["stress", "burnout", "anxiety"]
        }
    return {
        "student_id": student_id,
        "total_visits": 0,
        "recent_visits": 0,
        "last_visit_date": None,
        "reported_issues": []
    }

def get_survey_responses(student_id: str) -> Dict[str, Any]:
    """
    Fetches recent survey responses from the student.
    """
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "satisfaction_score": 2.5,  # Out of 5
            "stress_level": 4.5,  # Out of 5
            "workload_rating": 5.0,  # Out of 5 (overwhelming)
            "comments": "Feeling overwhelmed with coursework and personal issues."
        }
    return {
        "student_id": student_id,
        "satisfaction_score": 4.0,
        "stress_level": 2.0,
        "workload_rating": 3.0,
        "comments": "Everything is going well."
    }

def get_social_engagement(student_id: str) -> Dict[str, Any]:
    """
    Fetches social and campus engagement data.
    """
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "club_memberships": 0,
            "event_attendance_last_month": 0,
            "peer_interaction_score": 1.5  # Out of 5
        }
    return {
        "student_id": student_id,
        "club_memberships": 2,
        "event_attendance_last_month": 4,
        "peer_interaction_score": 4.0
    }
