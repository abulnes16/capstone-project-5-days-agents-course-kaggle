"""
This module defines the centralized MockDataStore.
It contains consistent mock data for multiple student profiles (High, Medium, Low risk)
to be used by all agents for testing and verification.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta

class MockDataStore:
    """
    A centralized store for mock student data.
    """
    
    _students = {
        "student_high_risk": {
            "profile": {
                "name": "John Doe",
                "risk_level": "High"
            },
            "attendance": {
                "total_classes": 40,
                "missed_classes": 10,
                "attendance_rate": 0.75,
                "recent_absences": 3,
                "last_attended": (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
            },
            "grades": {
                "current_gpa": 2.1,
                "failed_courses": 1,
                "missing_assignments": 4,
                "recent_grades": [
                    {"course": "Math 101", "grade": "D"},
                    {"course": "History 202", "grade": "C-"}
                ]
            },
            "lms": {
                "last_login": (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d"),
                "average_daily_time_minutes": 5,
                "resources_viewed_last_week": 0
            },
            "financial": {
                "tuition_paid": False,
                "financial_hold": True,
                "outstanding_balance": 1500.00
            },
            "counseling": {
                "total_visits": 5,
                "recent_visits": 3,
                "last_visit_date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
                "reported_issues": ["stress", "burnout", "anxiety"]
            },
            "surveys": {
                "satisfaction_score": 2.5,
                "stress_level": 4.5,
                "workload_rating": 5.0,
                "comments": "Feeling overwhelmed with coursework and personal issues."
            },
            "social": {
                "club_memberships": 0,
                "event_attendance_last_month": 0,
                "peer_interaction_score": 1.5
            },
            "academic_support": {
                "weak_subjects": [
                    {"subject": "Math 101", "grade": "D", "topic": "Calculus"},
                    {"subject": "History 202", "grade": "C-", "topic": "World War II"}
                ],
                "learning_style": "Visual",
                "preferences": ["Videos", "Diagrams", "Interactive simulations"]
            },
            "family": {
                "parent_name": "John Doe Sr.",
                "email": "parent@example.com",
                "phone": "+1-555-1234",
                "preferred_language": "English"
            }
        },
        "student_medium_risk": {
            "profile": {
                "name": "Jane Smith",
                "risk_level": "Medium"
            },
            "attendance": {
                "total_classes": 40,
                "missed_classes": 4,
                "attendance_rate": 0.90,
                "recent_absences": 1,
                "last_attended": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            },
            "grades": {
                "current_gpa": 2.8,
                "failed_courses": 0,
                "missing_assignments": 1,
                "recent_grades": [
                    {"course": "Math 101", "grade": "C+"},
                    {"course": "History 202", "grade": "B-"}
                ]
            },
            "lms": {
                "last_login": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
                "average_daily_time_minutes": 30,
                "resources_viewed_last_week": 5
            },
            "financial": {
                "tuition_paid": True,
                "financial_hold": False,
                "outstanding_balance": 0.0
            },
            "counseling": {
                "total_visits": 1,
                "recent_visits": 0,
                "last_visit_date": (datetime.now() - timedelta(days=45)).strftime("%Y-%m-%d"),
                "reported_issues": ["exam anxiety"]
            },
            "surveys": {
                "satisfaction_score": 3.5,
                "stress_level": 3.0,
                "workload_rating": 3.5,
                "comments": "Classes are hard but manageable."
            },
            "social": {
                "club_memberships": 1,
                "event_attendance_last_month": 2,
                "peer_interaction_score": 3.0
            },
            "academic_support": {
                "weak_subjects": [
                    {"subject": "Math 101", "grade": "C+", "topic": "Algebra"}
                ],
                "learning_style": "Auditory",
                "preferences": ["Lectures", "Podcasts", "Group discussions"]
            },
            "family": {
                "parent_name": "Mary Smith",
                "email": "mary.smith@example.com",
                "phone": "+1-555-5678",
                "preferred_language": "Spanish"
            }
        },
        "student_low_risk": {
            "profile": {
                "name": "Alice Johnson",
                "risk_level": "Low"
            },
            "attendance": {
                "total_classes": 40,
                "missed_classes": 0,
                "attendance_rate": 1.0,
                "recent_absences": 0,
                "last_attended": datetime.now().strftime("%Y-%m-%d")
            },
            "grades": {
                "current_gpa": 3.9,
                "failed_courses": 0,
                "missing_assignments": 0,
                "recent_grades": [
                    {"course": "Math 101", "grade": "A"},
                    {"course": "History 202", "grade": "A-"}
                ]
            },
            "lms": {
                "last_login": datetime.now().strftime("%Y-%m-%d"),
                "average_daily_time_minutes": 60,
                "resources_viewed_last_week": 15
            },
            "financial": {
                "tuition_paid": True,
                "financial_hold": False,
                "outstanding_balance": 0.0
            },
            "counseling": {
                "total_visits": 0,
                "recent_visits": 0,
                "last_visit_date": None,
                "reported_issues": []
            },
            "surveys": {
                "satisfaction_score": 4.8,
                "stress_level": 1.5,
                "workload_rating": 2.0,
                "comments": "Loving the semester so far!"
            },
            "social": {
                "club_memberships": 3,
                "event_attendance_last_month": 8,
                "peer_interaction_score": 5.0
            },
            "academic_support": {
                "weak_subjects": [],
                "learning_style": "Kinesthetic",
                "preferences": ["Labs", "Field trips", "Hands-on projects"]
            },
            "family": {
                "parent_name": "Robert Johnson",
                "email": "robert.j@example.com",
                "phone": "+1-555-9012",
                "preferred_language": "English"
            }
        }
    }

    @classmethod
    def get_student_data(cls, student_id: str, category: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves a specific category of data for a student.
        """
        student = cls._students.get(student_id)
        if not student:
            return None
        return student.get(category)
