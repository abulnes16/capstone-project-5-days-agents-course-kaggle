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
