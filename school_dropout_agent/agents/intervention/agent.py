"""
This module defines the InterventionCoordinatorAgent.
It is responsible for creating formal intervention records and notifying stakeholders.
It saves intervention plans to the database.
"""
from google.adk.agents.llm_agent import Agent
from school_dropout_agent.agents.intervention.tools import create_intervention, notify_stakeholder, get_active_interventions
from school_dropout_agent.agents.intervention.tools import create_intervention, notify_stakeholder, get_active_interventions

INTERVENTION_INSTRUCTION = """
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
1. Call `save_agent_result` with the full interventions JSON.
2. Return a BRIEF 1-sentence summary (e.g., "Created 2 interventions and notified counselor.").
"""


from school_dropout_agent.agents.orchestrator.tools import save_agent_result

class InterventionCoordinatorAgent(Agent):
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="intervention_coordinator_agent",
            description="Coordinates interventions and notifications.",
            instruction=INTERVENTION_INSTRUCTION,
            tools=[
                create_intervention,
                notify_stakeholder,
                get_active_interventions,
                save_agent_result
            ]
        )
        object.__setattr__(self, 'memory_service', memory_service)
