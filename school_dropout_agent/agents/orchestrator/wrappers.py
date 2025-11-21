import asyncio
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from school_dropout_agent.agents.risk_prediction.agent import RiskPredictionAgent
from school_dropout_agent.agents.intervention.agent import InterventionCoordinatorAgent
from school_dropout_agent.agents.emotional.agent import EmotionalBehavioralAgent
from school_dropout_agent.agents.academic_support.agent import AcademicSupportAgent
from school_dropout_agent.agents.family.agent import FamilyEngagementAgent
from school_dropout_agent.agents.monitoring.agent import MonitoringAgent

async def analyze_risk(student_id: str) -> str:
    """
    Runs the Risk Prediction Agent to analyze the student and save the assessment.
    """
    agent = RiskPredictionAgent()
    session_service = InMemorySessionService()
    await session_service.create_session(app_name="risk_prediction", user_id="system", session_id="risk_session")
    runner = Runner(agent=agent, session_service=session_service, app_name="risk_prediction")
    
    prompt = f"Analyze student {student_id}. You MUST call save_risk_assessment."
    message = Content(role="user", parts=[Part(text=prompt)])
    
    response_text = ""
    async for event in runner.run_async(new_message=message, user_id="system", session_id="risk_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    
    return response_text

async def check_emotional_state(student_id: str) -> str:
    """
    Runs the Emotional & Behavioral Agent.
    """
    agent = EmotionalBehavioralAgent()
    session_service = InMemorySessionService()
    await session_service.create_session(app_name="emotional", user_id="system", session_id="emotional_session")
    runner = Runner(agent=agent, session_service=session_service, app_name="emotional")
    
    prompt = f"Analyze emotional state for student {student_id}."
    message = Content(role="user", parts=[Part(text=prompt)])
    
    response_text = ""
    async for event in runner.run_async(new_message=message, user_id="system", session_id="emotional_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    return response_text

async def coordinate_intervention(student_id: str) -> str:
    """
    Runs the Intervention Coordinator to create and save interventions.
    """
    agent = InterventionCoordinatorAgent()
    session_service = InMemorySessionService()
    await session_service.create_session(app_name="intervention", user_id="system", session_id="intervention_session")
    runner = Runner(agent=agent, session_service=session_service, app_name="intervention")
    
    prompt = f"Create interventions for student {student_id}. You MUST save them."
    message = Content(role="user", parts=[Part(text=prompt)])
    
    response_text = ""
    async for event in runner.run_async(new_message=message, user_id="system", session_id="intervention_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    return response_text

async def provide_academic_support(student_id: str) -> str:
    agent = AcademicSupportAgent()
    session_service = InMemorySessionService()
    await session_service.create_session(app_name="academic_support", user_id="system", session_id="academic_session")
    runner = Runner(agent=agent, session_service=session_service, app_name="academic_support")
    prompt = f"Create study plan for student {student_id}."
    message = Content(role="user", parts=[Part(text=prompt)])
    response_text = ""
    async for event in runner.run_async(new_message=message, user_id="system", session_id="academic_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    return response_text

async def engage_family(student_id: str) -> str:
    agent = FamilyEngagementAgent()
    session_service = InMemorySessionService()
    await session_service.create_session(app_name="family", user_id="system", session_id="family_session")
    runner = Runner(agent=agent, session_service=session_service, app_name="family")
    prompt = f"Contact parents of student {student_id}."
    message = Content(role="user", parts=[Part(text=prompt)])
    response_text = ""
    async for event in runner.run_async(new_message=message, user_id="system", session_id="family_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    return response_text

async def monitor_progress(student_id: str) -> str:
    agent = MonitoringAgent()
    session_service = InMemorySessionService()
    await session_service.create_session(app_name="monitoring", user_id="system", session_id="monitoring_session")
    runner = Runner(agent=agent, session_service=session_service, app_name="monitoring")
    prompt = f"Check progress for student {student_id}."
    message = Content(role="user", parts=[Part(text=prompt)])
    response_text = ""
    async for event in runner.run_async(new_message=message, user_id="system", session_id="monitoring_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    return response_text
