"""
This module defines the Event entity.
It represents significant occurrences in the student's lifecycle that might trigger analysis or be recorded in history.
Used for event-driven updates and logging.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict

@dataclass
class Event:
    event_id: str
    event_type: str
    timestamp: datetime
    payload: Dict[str, Any] = field(default_factory=dict)
    source: str = "System"
