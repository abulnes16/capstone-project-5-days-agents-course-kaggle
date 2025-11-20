from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

@dataclass
class Student:
    student_id: str
    first_name: str
    last_name: str
    email: str
    enrollment_status: str  # 'Active', 'Probation', 'Withdrawn'
    major: str
    enrollment_date: date
    
    # Additional fields can be added as needed
    metadata: dict = field(default_factory=dict)
