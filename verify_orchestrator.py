import sys
import os
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.getcwd())

# Load .env
env_path = os.path.join(os.getcwd(), "school_dropout_agent", ".env")
load_dotenv(env_path)

APP_NAME = "dropout_prevention"

import asyncio
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from school_dropout_agent.agents.orchestrator.agent import DropoutPreventionOrchestrator
from school_dropout_agent.infrastructure.memory.database_memory import DatabaseMemoryService
from school_dropout_agent.core.session.session_manager import SessionManager
from school_dropout_agent.infrastructure.database.database import init_db

async def test_orchestrator():
    """Test the orchestrator agent with memory and session management."""
    
    print("="*60)
    print("Dropout Prevention Orchestrator - Verification")
    print("="*60)
    
    # Initialize database
    print("\n1. Initializing database...")
    init_db()
    
    # Seed student data
    print("   Seeding student data...")
    seed_memory = DatabaseMemoryService()
    seed_memory.store_student_profile("risk_case_1", {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "enrollment_status": "Active",
        "major": "Computer Science"
    })
    
    # Create services
    print("2. Creating memory and session services...")
    memory_service = DatabaseMemoryService()
    session_service = InMemorySessionService()
    session_manager = SessionManager(session_service, memory_service)
    
    # Create orchestrator
    print("3. Creating orchestrator agent...")
    orchestrator = DropoutPreventionOrchestrator()
    
    # Create session for student analysis
    student_id = "risk_case_1"
    print(f"4. Creating session for student: {student_id}...")
    
    session = await session_manager.create_student_session(
        app_name=APP_NAME,
        user_id="counselor_1",
        student_id=student_id,
        session_id="orch_session_1"
    )
    
    print(f"   Session created: {session.id}")
    print(f"   Initial state: {session.state}")
    
    # Create runner
    runner = Runner(agent=orchestrator, session_service=session_service, app_name=APP_NAME)
    
    # Test 1: Complete student analysis
    print("\n" + "="*60)
    print("TEST 1: Complete Student Analysis")
    print("="*60)
    
    prompt = f"Please analyze student {student_id} for dropout risk and create appropriate interventions."
    message = Content(role="user", parts=[Part(text=prompt)])
    
    print(f"\nPrompt: {prompt}\n")
    print("Orchestrator Response:")
    print("-" * 60)
    
    async for event in runner.run_async(new_message=message, user_id="counselor_1", session_id="orch_session_1"):
        # Print all attributes to debug
        # print(f"DEBUG: Event type: {type(event)}")
        
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
                elif part.function_call:
                    print(f"\n[Tool Call: {part.function_call.name}]", flush=True)
                elif part.function_response:
                    print(f"\n[Tool Result: {part.function_response.name}]", flush=True)
    
    print("\n" + "-" * 60)
    
    # Check session state
    print("\n5. Checking session state...")
    final_state = await session_manager.get_session_state(
        app_name=APP_NAME,
        user_id="counselor_1",
        session_id="orch_session_1"
    )
    print(f"   Final session state: {final_state}")
    
    # Check memory persistence
    print("\n6. Checking memory persistence...")
    student_history = memory_service.retrieve_student_history(student_id)
    if student_history:
        print(f"   Student history retrieved from database:")
        print(f"   - Risk Level: {student_history.get('risk_profile', {}).get('risk_level', 'N/A')}")
        print(f"   - Interventions: {len(student_history.get('interventions', []))}")
    else:
        print("   No student history found in database")
    
    # Test 2: Follow-up query (session resumption)
    print("\n" + "="*60)
    print("TEST 2: Follow-up Query (Session Resumption)")
    print("="*60)
    
    followup_prompt = f"What interventions were created for student {student_id}?"
    followup_message = Content(role="user", parts=[Part(text=followup_prompt)])
    
    print(f"\nPrompt: {followup_prompt}\n")
    print("Orchestrator Response:")
    print("-" * 60)
    
    async for event in runner.run_async(new_message=followup_message, user_id="counselor_1", session_id="orch_session_1"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    
    print("\n" + "-" * 60)
    
    print("\n" + "="*60)
    print("Verification Complete!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(test_orchestrator())
