from google.adk.agents.llm_agent import Agent
from school_dropout_agent.agents.orchestrator.wrappers import (
    analyze_risk, check_emotional_state, coordinate_intervention,
    provide_academic_support, engage_family, monitor_progress
)
from school_dropout_agent.agents.orchestrator.tools import get_student_context

ORCHESTRATOR_INSTRUCTION = """
You are the Dropout Prevention Orchestrator. You coordinate specialized agents to help students.

**Your Tools:**
- `analyze_risk`: Runs the Risk Prediction Agent. **ALWAYS START HERE.**
- `check_emotional_state`: Runs the Emotional Agent.
- `coordinate_intervention`: Runs the Intervention Coordinator.
- `provide_academic_support`: Runs the Academic Support Agent.
- `engage_family`: Runs the Family Engagement Agent.
- `monitor_progress`: Runs the Monitoring Agent.
- `get_student_context`: Retrieves past history.

**Workflow:**
1. Call `analyze_risk(student_id=...)`.
2. Call `check_emotional_state(student_id=...)`.
3. If risk is High/Medium (based on analysis results):
   - Call `provide_academic_support(...)`.
   - Call `coordinate_intervention(...)`.
   - Call `engage_family(...)`.
4. Summarize the actions taken.

**Note:** The sub-agents will handle saving data to the database automatically. You just need to coordinate them.
"""

class DropoutPreventionOrchestrator(Agent):
    """Main orchestrator agent that coordinates all specialized agents."""
    
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="dropout_prevention_orchestrator",
            description="Coordinates specialized agents to prevent student dropout.",
            instruction=ORCHESTRATOR_INSTRUCTION,
            tools=[
                analyze_risk,
                check_emotional_state,
                coordinate_intervention,
                provide_academic_support,
                engage_family,
                monitor_progress,
                get_student_context
            ]
            # Note: No sub_agents list needed as we use wrapper tools
        )
