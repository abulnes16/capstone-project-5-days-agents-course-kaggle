"""
This module defines the DropoutPreventionOrchestrator agent.
It acts as a Router, deciding whether to run a full analysis pipeline or answer specific questions based on existing data.
"""
from google.adk.agents.llm_agent import Agent
from school_dropout_agent.agents.orchestrator.pipeline import FullAnalysisPipeline
from school_dropout_agent.agents.summary.agent import FinalSummaryAgent

ROUTER_INSTRUCTION = """
You are the Dropout Prevention Orchestrator. You are the main interface for the system.

**Your Capabilities:**
1. **Run Full Analysis**: If the user asks to analyze a student, assess risk, or create interventions, delegate to `full_analysis_pipeline`.
2. **Provide Summary**: If the user asks about the results of the last assessment, or wants a summary of what happened, delegate to `final_summary_agent`.

**Routing Logic:**
- "Analyze student X" -> `full_analysis_pipeline`
- "Check risk for student Y" -> `full_analysis_pipeline`
- "What was the result?" -> `final_summary_agent`
- "Show me the summary" -> `final_summary_agent`

**Important:**
- Do NOT run the full pipeline if the user is just asking about previous results.
- Delegate to the appropriate sub-agent based on the user's intent.
"""

class DropoutPreventionOrchestrator(Agent):
    """
    Router agent that directs user requests to the appropriate sub-agent or pipeline.
    """
    
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        # Initialize sub-agents
        sub_agents = [
            FullAnalysisPipeline(memory_service=memory_service, model_name=model_name),
            FinalSummaryAgent(memory_service=memory_service, model_name=model_name)
        ]
        
        super().__init__(
            model=model_name,
            name="dropout_prevention_orchestrator",
            description="Main router that coordinates student analysis and reporting.",
            instruction=ROUTER_INSTRUCTION,
            sub_agents=sub_agents
        )
        
        # Store memory service after super().__init__()
        object.__setattr__(self, 'memory_service', memory_service)
