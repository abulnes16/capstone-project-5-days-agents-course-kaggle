"""
This module defines the MonitoringAgent.
It tracks the progress of interventions and student performance over time.
Used for follow-up queries and long-term tracking.
"""
from google.adk.agents.llm_agent import Agent
from .tools import get_intervention_outcome, compare_metrics, record_outcome

MONITORING_AGENT_INSTRUCTION = """
You are an expert Monitoring Agent for a university dropout prevention system.
Your goal is to track the effectiveness of interventions and adjust plans as needed.

You have access to the following tools:
- `get_intervention_outcome`: Check the status and outcome of an intervention.
- `compare_metrics`: Compare student metrics before and after intervention.
- `record_outcome`: Record the final outcome of an intervention.

**Monitoring Criteria:**
1. Compare attendance, GPA, and LMS activity before and after intervention.
2. Determine if the intervention was effective (metrics improved).
3. Recommend continuation, adjustment, or closure of the intervention.

**Output Format:**
1. Call `save_agent_result` with the full monitoring report JSON.
2. Return a BRIEF 1-sentence summary (e.g., "Intervention effective, attendance improved by 10%.").
"""

from school_dropout_agent.agents.orchestrator.tools import save_agent_result

class MonitoringAgent(Agent):
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="monitoring_agent",
            description="Tracks intervention effectiveness and outcomes.",
            instruction=MONITORING_AGENT_INSTRUCTION,
            tools=[
                get_intervention_outcome,
                compare_metrics,
                record_outcome,
                save_agent_result
            ]
        )
        object.__setattr__(self, 'memory_service', memory_service)
