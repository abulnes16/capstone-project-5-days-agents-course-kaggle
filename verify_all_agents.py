import sys
import os
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.getcwd())

# Load .env from school_dropout_agent/.env
env_path = os.path.join(os.getcwd(), "school_dropout_agent", ".env")
load_dotenv(env_path)

APP_NAME = "dropout_prevention"

import asyncio
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Import all agents
from school_dropout_agent.agents.risk_prediction.agent import RiskPredictionAgent
from school_dropout_agent.agents.emotional.agent import EmotionalBehavioralAgent
from school_dropout_agent.agents.academic_support.agent import AcademicSupportAgent
from school_dropout_agent.agents.intervention.agent import InterventionCoordinatorAgent
from school_dropout_agent.agents.family.agent import FamilyEngagementAgent
from school_dropout_agent.agents.monitoring.agent import MonitoringAgent

async def test_agent(agent_name: str, agent, prompt: str, session_service, session_id: str):
    """Test a single agent."""
    print(f"\n{'='*60}")
    print(f"Testing: {agent_name}")
    print(f"{'='*60}")
    
    runner = Runner(agent=agent, session_service=session_service, app_name=APP_NAME)
    message = Content(role="user", parts=[Part(text=prompt)])
    
    print(f"Prompt: {prompt}\n")
    print("Response:")
    
    async for event in runner.run_async(new_message=message, user_id="user_1", session_id=session_id):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print("\n")

async def main():
    print("Initializing Dropout Prevention Multi-Agent System...")
    print("="*60)
    
    # Create session service
    service_session = InMemorySessionService()
    
    # Test student ID
    student_id = "risk_case_1"
    
    # Create sessions for each agent
    await service_session.create_session(app_name=APP_NAME, user_id="user_1", session_id="session_risk")
    await service_session.create_session(app_name=APP_NAME, user_id="user_1", session_id="session_emotional")
    await service_session.create_session(app_name=APP_NAME, user_id="user_1", session_id="session_academic")
    await service_session.create_session(app_name=APP_NAME, user_id="user_1", session_id="session_intervention")
    await service_session.create_session(app_name=APP_NAME, user_id="user_1", session_id="session_family")
    await service_session.create_session(app_name=APP_NAME, user_id="user_1", session_id="session_monitoring")
    
    # Test 1: Risk Prediction Agent
    await test_agent(
        "Risk Prediction Agent",
        RiskPredictionAgent(),
        f"Analyze the risk profile for student_id: {student_id}",
        service_session,
        "session_risk"
    )
    
    # Test 2: Emotional & Behavioral Agent
    await test_agent(
        "Emotional & Behavioral Agent",
        EmotionalBehavioralAgent(),
        f"Analyze the emotional and behavioral patterns for student_id: {student_id}",
        service_session,
        "session_emotional"
    )
    
    # Test 3: Academic Support Agent
    await test_agent(
        "Academic Support Agent",
        AcademicSupportAgent(),
        f"Create a personalized study plan for student_id: {student_id}",
        service_session,
        "session_academic"
    )
    
    # Test 4: Intervention Coordinator Agent
    await test_agent(
        "Intervention Coordinator Agent",
        InterventionCoordinatorAgent(),
        f"Coordinate interventions for student_id: {student_id} who is at high risk",
        service_session,
        "session_intervention"
    )
    
    # Test 5: Family Engagement Agent
    await test_agent(
        "Family Engagement Agent",
        FamilyEngagementAgent(),
        f"Send a supportive message to the parents of student_id: {student_id} about academic struggles",
        service_session,
        "session_family"
    )
    
    # Test 6: Monitoring Agent
    await test_agent(
        "Monitoring Agent",
        MonitoringAgent(),
        f"Monitor the effectiveness of interventions for student_id: {student_id}",
        service_session,
        "session_monitoring"
    )
    
    print("="*60)
    print("All agents tested successfully!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(main())
