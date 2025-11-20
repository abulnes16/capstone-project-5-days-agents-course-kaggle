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
Return a JSON object with:
- `risk_score`: Float between 0.0 (Low) and 1.0 (Critical).
- `risk_level`: "Low", "Medium", "High".
- `factors`: List of strings describing the specific risk factors found.
- `summary`: A brief explanation of the assessment.

Example:
{
  "risk_score": 0.85,
  "risk_level": "High",
  "factors": ["Low Attendance (75%)", "Financial Hold"],
  "summary": "Student is at high risk due to consistent absences and an active financial hold."
}
"""

class RiskPredictionAgent(Agent):
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="risk_prediction_agent",
            description="Analyzes student data to predict dropout risk.",
            instruction=RISK_AGENT_INSTRUCTION,
            tools=[
                get_student_attendance,
                get_student_grades,
                get_lms_activity,
                get_financial_status
            ]
        )