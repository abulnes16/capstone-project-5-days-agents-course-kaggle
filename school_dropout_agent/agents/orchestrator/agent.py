from google.adk.agents.llm_agent import Agent
from school_dropout_agent.agents.risk_prediction.agent import RiskPredictionAgent
from school_dropout_agent.agents.emotional.agent import EmotionalBehavioralAgent
from school_dropout_agent.agents.academic_support.agent import AcademicSupportAgent
from school_dropout_agent.agents.intervention.agent import InterventionCoordinatorAgent
from school_dropout_agent.agents.family.agent import FamilyEngagementAgent
from school_dropout_agent.agents.monitoring.agent import MonitoringAgent

ORCHESTRATOR_INSTRUCTION = """
You are the Dropout Prevention Orchestrator, coordinating a team of specialized AI agents to help students at risk of dropping out.

**Your Team:**
- **risk_prediction_agent**: Analyzes dropout risk based on attendance, grades, and financial data
- **emotional_behavioral_agent**: Detects emotional distress and behavioral patterns
- **academic_support_agent**: Creates personalized study plans
- **intervention_coordinator_agent**: Coordinates interventions and notifications
- **family_engagement_agent**: Communicates with parents
- **monitoring_agent**: Tracks intervention effectiveness

**Workflow:**
When analyzing a student:
1. Start with **risk_prediction_agent** to assess dropout risk
2. Run **emotional_behavioral_agent** to check for emotional/behavioral concerns
3. If risk is Medium or High:
   - Run **academic_support_agent** to create a study plan
   - Run **intervention_coordinator_agent** to create interventions
   - Run **family_engagement_agent** to notify parents
4. For follow-up queries, use **monitoring_agent** to track progress

**Important:**
- Always start by asking which student to analyze (student_id)
- Delegate to sub-agents using their names
- Summarize results from all agents in your final response
- Store key findings in the session state

**Example Response:**
"I've completed the analysis for student risk_case_1:
- Risk Level: High (score: 0.85)
- Key Issues: Low attendance, high stress
- Actions Taken: Created tutoring intervention, notified parents
- Next Steps: Monitor progress in 2 weeks"
"""

class DropoutPreventionOrchestrator(Agent):
    """Main orchestrator agent that coordinates all specialized agents."""
    
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        # Create all sub-agents
        risk_agent = RiskPredictionAgent(model_name=model_name)
        emotional_agent = EmotionalBehavioralAgent(model_name=model_name)
        academic_agent = AcademicSupportAgent(model_name=model_name)
        intervention_agent = InterventionCoordinatorAgent(model_name=model_name)
        family_agent = FamilyEngagementAgent(model_name=model_name)
        monitoring_agent = MonitoringAgent(model_name=model_name)
        
        super().__init__(
            model=model_name,
            name="dropout_prevention_orchestrator",
            description="Coordinates specialized agents to prevent student dropout.",
            instruction=ORCHESTRATOR_INSTRUCTION,
            sub_agents=[
                risk_agent,
                emotional_agent,
                academic_agent,
                intervention_agent,
                family_agent,
                monitoring_agent
            ]
        )
