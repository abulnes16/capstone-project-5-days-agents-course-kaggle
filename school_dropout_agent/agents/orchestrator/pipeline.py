"""
This module defines the FullAnalysisPipeline.
It uses SequentialAgent to ensure all sub-agents are called in the correct order for a full analysis.
"""
from google.adk.agents.sequential_agent import SequentialAgent
from school_dropout_agent.agents.risk_prediction.agent import RiskPredictionAgent
from school_dropout_agent.agents.emotional.agent import EmotionalBehavioralAgent
from school_dropout_agent.agents.academic_support.agent import AcademicSupportAgent
from school_dropout_agent.agents.intervention.agent import InterventionCoordinatorAgent
from school_dropout_agent.agents.family.agent import FamilyEngagementAgent
from school_dropout_agent.agents.monitoring.agent import MonitoringAgent
from school_dropout_agent.agents.summary.agent import FinalSummaryAgent

class FullAnalysisPipeline(SequentialAgent):
    """
    Sequential pipeline that runs the full student analysis workflow.
    """
    
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        # Initialize sub-agents with memory service
        # These will be called in sequence automatically
        sub_agents = [
            RiskPredictionAgent(memory_service=memory_service, model_name=model_name),
            EmotionalBehavioralAgent(memory_service=memory_service, model_name=model_name),
            AcademicSupportAgent(memory_service=memory_service, model_name=model_name),
            InterventionCoordinatorAgent(memory_service=memory_service, model_name=model_name),
            FamilyEngagementAgent(memory_service=memory_service, model_name=model_name),
            FinalSummaryAgent(memory_service=memory_service, model_name=model_name)
        ]
        
        super().__init__(
            name="full_analysis_pipeline",
            description="Runs a complete analysis of the student, including risk prediction, emotional check, academic support, interventions, and family engagement.",
            sub_agents=sub_agents
        )
        
        # Store memory service after super().__init__()
        object.__setattr__(self, 'memory_service', memory_service)
