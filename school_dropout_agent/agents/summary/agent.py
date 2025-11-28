"""
This module defines the FinalSummaryAgent.
It aggregates results from all other agents and produces a comprehensive final report.
"""
from google.adk.agents.llm_agent import Agent
from school_dropout_agent.agents.orchestrator.tools import get_all_agent_results

FINAL_SUMMARY_INSTRUCTION = """
You are the Final Summary Agent for the Dropout Prevention System.
Your goal is to review the work of all previous agents and provide a comprehensive final report.

**Your Task:**
1. Identify the `student_id` from the conversation context if possible.
2. Call `get_all_agent_results(student_id=...)` to retrieve the detailed JSON outputs.
   - If `student_id` is known, PASS IT to the tool. This allows retrieving past data from the database if the current session is empty.
3. Synthesize this information into a clear, actionable summary for the user.
4. Highlight key risks, interventions created, and family communication status.

**Output Format:**
Provide a structured markdown summary:

## Student Analysis Summary
**Risk Level:** [High/Medium/Low] (Score: X.XX)
**Key Factors:** [List factors]

### Actions Taken
- **Emotional:** [Summary of emotional state]
- **Academic:** [Summary of study plan]
- **Interventions:** [List interventions created]
- **Family:** [Communication status]

### Next Steps
[Recommendations for the user]
"""

class FinalSummaryAgent(Agent):
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="final_summary_agent",
            description="Aggregates results and produces final report.",
            instruction=FINAL_SUMMARY_INSTRUCTION,
            tools=[get_all_agent_results]
        )
        object.__setattr__(self, 'memory_service', memory_service)
