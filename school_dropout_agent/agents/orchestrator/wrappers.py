"""
This module defines wrapper functions for running sub-agents.
Each wrapper creates a dedicated `Runner` and `Session` (shared) for a sub-agent.
This ensures that sub-agents execute in their own context and can reliably call their own tools (including persistence).
"""
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.agents.llm_agent import Agent
from google.genai.types import Content, Part

from school_dropout_agent.agents.risk_prediction.agent import RiskPredictionAgent
from school_dropout_agent.agents.intervention.agent import InterventionCoordinatorAgent
from school_dropout_agent.agents.emotional.agent import EmotionalBehavioralAgent
from school_dropout_agent.agents.academic_support.agent import AcademicSupportAgent
from school_dropout_agent.agents.family.agent import FamilyEngagementAgent
from school_dropout_agent.agents.monitoring.agent import MonitoringAgent

# Shared session service instance
_shared_session_service = InMemorySessionService()

async def _run_sub_agent(agent: Agent, app_name: str, prompt: str) -> str:
    """
    Generic helper to run a sub-agent with the shared session.
    """
    session_service = _shared_session_service
    
    # Create session if not exists (idempotent)
    try:
        await session_service.create_session(app_name=app_name, user_id="system", session_id="shared_session")
    except ValueError:
        pass # Session might already exist
        
    runner = Runner(agent=agent, session_service=session_service, app_name=app_name)
    
    message = Content(role="user", parts=[Part(text=prompt)])
    
    response_text = ""
    async for event in runner.run_async(new_message=message, user_id="system", session_id="shared_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    
    return response_text

async def analyze_risk(student_id: str) -> str:
    """
    Runs the Risk Prediction Agent to analyze the student and save the assessment.
    """
    return await _run_sub_agent(
        agent=RiskPredictionAgent(),
        app_name="risk_prediction",
        prompt=f"Analyze student {student_id}. You MUST call save_risk_assessment."
    )

async def check_emotional_state(student_id: str) -> str:
    """
    Runs the Emotional & Behavioral Agent.
    """
    return await _run_sub_agent(
        agent=EmotionalBehavioralAgent(),
        app_name="emotional",
        prompt=f"Analyze emotional state for student {student_id}."
    )

async def coordinate_intervention(student_id: str) -> str:
    """
    Runs the Intervention Coordinator to create and save interventions.
    """
    return await _run_sub_agent(
        agent=InterventionCoordinatorAgent(),
        app_name="intervention",
        prompt=f"Create interventions for student {student_id}. You MUST save them."
    )

async def provide_academic_support(student_id: str) -> str:
    return await _run_sub_agent(
        agent=AcademicSupportAgent(),
        app_name="academic_support",
        prompt=f"Create study plan for student {student_id}."
    )

async def engage_family(student_id: str) -> str:
    return await _run_sub_agent(
        agent=FamilyEngagementAgent(),
        app_name="family",
        prompt=f"Contact parents of student {student_id}."
    )

async def monitor_progress(student_id: str) -> str:
    return await _run_sub_agent(
        agent=MonitoringAgent(),
        app_name="monitoring",
        prompt=f"Check progress for student {student_id}."
    )
