"""
This module defines tools for the Academic Support Agent.
It provides functionality to create study plans and retrieve learning resources.
"""
from typing import Dict, Any, List

from school_dropout_agent.infrastructure.mock_data import MockDataStore

def get_weak_subjects(student_id: str) -> Dict[str, Any]:
    """
    Identifies subjects where the student is struggling.
    """
    data = MockDataStore.get_student_data(student_id, "academic_support")
    if data:
        return {
            "student_id": student_id,
            "weak_subjects": data.get("weak_subjects", [])
        }

    return {
        "student_id": student_id,
        "weak_subjects": []
    }

def get_learning_style(student_id: str) -> Dict[str, Any]:
    """
    Retrieves the student's preferred learning style.
    """
    data = MockDataStore.get_student_data(student_id, "academic_support")
    if data:
        return {
            "student_id": student_id,
            "learning_style": data.get("learning_style", "Visual"),
            "preferences": data.get("preferences", [])
        }

    return {
        "student_id": student_id,
        "learning_style": "Visual",
        "preferences": ["Videos", "Diagrams", "Interactive simulations"]
    }

def get_study_resources(subject: str, topic: str) -> Dict[str, Any]:
    """
    Fetches relevant study resources for a given subject and topic.
    """
    # Mock data - in production, this would query a resource database
    return {
        "subject": subject,
        "topic": topic,
        "resources": [
            {"type": "Video", "title": f"{topic} Explained", "url": "https://example.com/video"},
            {"type": "Practice Problems", "title": f"{topic} Exercises", "url": "https://example.com/exercises"},
            {"type": "Tutorial", "title": f"{topic} Step-by-Step", "url": "https://example.com/tutorial"}
        ]
    }
