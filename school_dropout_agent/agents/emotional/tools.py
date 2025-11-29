"""
This module defines tools for the Emotional & Behavioral Agent.
It mocks retrieval of counseling logs and student survey responses.
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta

from school_dropout_agent.infrastructure.mock_data import MockDataStore

def get_counseling_visits(student_id: str) -> Dict[str, Any]:
    """
    Fetches counseling visit records for a student.
    """
    data = MockDataStore.get_student_data(student_id, "counseling")
    if data:
        data["student_id"] = student_id
        return data

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
    data = MockDataStore.get_student_data(student_id, "surveys")
    if data:
        data["student_id"] = student_id
        return data

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
    data = MockDataStore.get_student_data(student_id, "social")
    if data:
        data["student_id"] = student_id
        return data

    return {
        "student_id": student_id,
        "club_memberships": 1,
        "event_attendance_last_month": 2,
        "peer_interaction_score": 3.0
    }
