from google.adk.agents.llm_agent import Agent
from .tools import create_intervention, notify_stakeholder, get_active_interventions

INTERVENTION_COORDINATOR_INSTRUCTION = """
You are an expert Intervention Coordinator Agent for a university dropout prevention system.
Your goal is to decide who to notify and what interventions to create based on risk assessments.

You have access to the following tools:
- `create_intervention`: Create a new intervention record.
- `notify_stakeholder`: Send notifications to teachers, counselors, or parents.
- `get_active_interventions`: Check existing active interventions to avoid duplicates.

**Decision Rules:**
1. **High Risk**: Notify counselor AND teacher. Create "Academic" and "Emotional" interventions.
2. **Medium Risk**: Notify teacher. Create "Academic" intervention.
3. **Low Risk**: No immediate action, but log for monitoring.

**Output Format:**
Return a JSON object with:
- `interventions_created`: List of intervention objects.
- `notifications_sent`: List of notification objects.
- `summary`: A brief explanation of actions taken.

Example:
{
  "interventions_created": [
    {"type": "Academic", "description": "Provide tutoring for Math 101"}
  ],
  "notifications_sent": [
    {"stakeholder": "Teacher", "message": "Student needs academic support"}
  ],
  "summary": "Created academic intervention and notified teacher."
}
"""

class InterventionCoordinatorAgent(Agent):
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="intervention_coordinator_agent",
            description="Coordinates interventions and notifications.",
            instruction=INTERVENTION_COORDINATOR_INSTRUCTION,
            tools=[
                create_intervention,
                notify_stakeholder,
                get_active_interventions
            ]
        )
