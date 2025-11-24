"""
This module defines the RiskProfile entity.
It encapsulates the result of a risk assessment, including the calculated score, level, and specific factors.
Used by the RiskPredictionAgent to return analysis results and by the Orchestrator to make decisions.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class RiskProfile:
    student_id: str
    risk_score: float  # 0.0 (Low) to 1.0 (High)
    risk_level: str # 'Low', 'Medium', 'High'
    last_updated: datetime
    risk_factors: List[str] = field(default_factory=list)
    
    def update_score(self, new_score: float, factors: List[str]):
        self.risk_score = new_score
        self.risk_factors = factors
        self.last_updated = datetime.now()
        self.risk_level = self._calculate_level(new_score)

    def _calculate_level(self, score: float) -> str:
        if score < 0.3:
            return 'Low'
        elif score < 0.7:
            return 'Medium'
        else:
            return 'High'
