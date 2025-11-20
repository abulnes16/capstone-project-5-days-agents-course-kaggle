from typing import Dict, Any, List

def get_weak_subjects(student_id: str) -> Dict[str, Any]:
    """
    Identifies subjects where the student is struggling.
    """
    if student_id == "risk_case_1":
        return {
            "student_id": student_id,
            "weak_subjects": [
                {"subject": "Math 101", "grade": "D", "topic": "Calculus"},
                {"subject": "History 202", "grade": "C-", "topic": "World War II"}
            ]
        }
    return {
        "student_id": student_id,
        "weak_subjects": []
    }

def get_learning_style(student_id: str) -> Dict[str, Any]:
    """
    Retrieves the student's preferred learning style.
    """
    # Mock data - in production, this would come from a student profile
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
