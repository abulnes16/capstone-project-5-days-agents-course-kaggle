"""
This module defines the RiskPredictionAgent.
It analyzes student data (attendance, grades, LMS, financial) to calculate a dropout risk score.
It is responsible for saving the risk assessment to the database.
"""
from google.adk.agents.llm_agent import Agent
from .tools import get_student_attendance, get_student_grades, get_lms_activity, get_financial_status


RISK_AGENT_INSTRUCTION = """
You are an expert Risk Prediction Agent for a university dropout prevention system.
Your goal is to analyze a student's data and determine their risk of dropping out.

You have access to the following tools:
- `get_student_attendance`: Check attendance patterns.
- `get_student_grades`: Check academic performance.
- `get_lms_activity`: Check engagement with the Learning Management System.
- `get_financial_status`: Check for financial holds.

**Risk Factors to Look For:**
1. Attendance < 80% or recent absences.
2. GPA < 2.5 or failing grades.
3. No LMS login in > 7 days.
4. Unpaid tuition or financial holds.

**Output Format:**
1. Call `save_risk_assessment` to save to database.
2. Call `save_agent_result` with the full JSON analysis (risk_score, level, factors, etc.).
3. Return a BRIEF 1-sentence summary (e.g., "Identified High Risk (0.85) due to attendance and grades.").
"""

from school_dropout_agent.agents.orchestrator.tools import save_risk_assessment, save_agent_result

class RiskPredictionAgent(Agent):
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="risk_prediction_agent",
            description="Analyzes student data to predict dropout risk.",
            instruction=RISK_AGENT_INSTRUCTION,
            tools=[
                get_student_attendance,
                get_student_grades,
                get_lms_activity,
                get_financial_status,
                save_risk_assessment,
                save_agent_result
            ]
        )
        object.__setattr__(self, 'memory_service', memory_service)