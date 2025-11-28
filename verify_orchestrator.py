import sys
import os
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.getcwd())

# Load .env
env_path = os.path.join(os.getcwd(), "school_dropout_agent", ".env")
load_dotenv(env_path)

APP_NAME = "dropout_prevention"

"""
This script verifies the end-to-end workflow of the School Dropout Prevention System.
It initializes the database, seeds mock data, runs the Orchestrator to analyze a student,
and verifies that risk assessments and interventions are correctly persisted to the database.
"""
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
    if os.path.exists("school_dropout_agent.db"):
        os.remove("school_dropout_agent.db")
    init_db()
    
    # Seed student data
    print("   Seeding student data...")
    seed_memory = DatabaseMemoryService()
    seed_memory.store_student_profile("student_high_risk", {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "enrollment_status": "Active",
        "major": "Computer Science"
    })
    seed_memory.store_student_profile("student_low_risk", {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.j@example.com",
        "enrollment_status": "Active",
        "major": "Biology"
    })
    
    # Create services
    print("2. Creating memory and session services...")
    memory_service = DatabaseMemoryService()
    session_service = InMemorySessionService()
    session_manager = SessionManager(session_service, memory_service)
    
    # Create orchestrator
    print("3. Creating orchestrator agent...")
    orchestrator = DropoutPreventionOrchestrator(memory_service=memory_service)
    
    # Create Sessions
    print("4. Creating sessions...")
    await session_manager.create_student_session(
        app_name=APP_NAME, 
        user_id="counselor_1", 
        student_id="student_high_risk",
        session_id="orch_session_high"
    )
    await session_manager.create_student_session(
        app_name=APP_NAME, 
        user_id="counselor_1", 
        student_id="student_low_risk",
        session_id="orch_session_low"
    )
    
    print(f"   Sessions created: orch_session_high, orch_session_low")
    
    # Create runner
    runner = Runner(agent=orchestrator, session_service=session_service, app_name=APP_NAME)
    
    # Test 1: Complete student analysis
    print("\n" + "="*60)
    print("TEST 1: Complete Student Analysis")
    print("="*60)
    
    prompt = "Please analyze student student_high_risk for dropout risk and create appropriate interventions."
    message = Content(role="user", parts=[Part(text=prompt)])
    
    print(f"\nPrompt: {prompt}\n")
    print("Orchestrator Response:")
    
    message = Content(role="user", parts=[Part(text=prompt)])
    
    print("Orchestrator Response:")
    print("-" * 60)
    async for event in runner.run_async(new_message=message, user_id="counselor_1", session_id="orch_session_high"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print("\n" + "-" * 60)
    
    # Verify Persistence
    print("\nChecking memory persistence for student_high_risk...")
    history = memory_service.retrieve_student_history("student_high_risk")
    if history:
        print("   Student history retrieved from database:")
        if history.get("risk_profile"):
            print(f"   - Risk Level: {history['risk_profile'].get('risk_level')}")
        print(f"   - Interventions: {len(history.get('interventions', []))}")
    else:
        print("   [ERROR] No student history found in database!")

    print("\n" + "="*60)
    print("TEST 2: Low Risk Student Analysis (student_low_risk)")
    print("="*60)
    
    prompt_low = "Please analyze student student_low_risk for dropout risk."
    print(f"\nPrompt: {prompt_low}\n")
    
    message_low = Content(role="user", parts=[Part(text=prompt_low)])
    
    print("Orchestrator Response:")
    print("-" * 60)
    async for event in runner.run_async(new_message=message_low, user_id="counselor_1", session_id="orch_session_low"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print("\n" + "-" * 60)

    print("\n" + "="*60)
    print("TEST 3: Summary Request (student_high_risk)")
    print("="*60)
    
    prompt_summary = "What was the result of the analysis for student_high_risk?"
    print(f"\nPrompt: {prompt_summary}\n")
    
    message_summary = Content(role="user", parts=[Part(text=prompt_summary)])
    
    print("Orchestrator Response:")
    print("-" * 60)
    async for event in runner.run_async(new_message=message_summary, user_id="counselor_1", session_id="orch_session_high"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print("\n" + "-" * 60)

    print("\n" + "-" * 60)

    # Test 4: Summary Request with Empty Shared State (Database Fallback)
    print("\n" + "="*60)
    print("TEST 4: Summary Request with Empty Shared State (Database Fallback)")
    print("="*60)
    
    # Clear Shared State to force DB fallback
    from school_dropout_agent.core.session.shared_state import SharedStateStore
    SharedStateStore.clear()
    print("   [Shared State Cleared]")
    
    prompt_fallback = "Can you give me a summary for student_high_risk again? I lost the previous one."
    print(f"\nPrompt: {prompt_fallback}\n")
    
    message_fallback = Content(role="user", parts=[Part(text=prompt_fallback)])
    
    print("Orchestrator Response:")
    print("-" * 60)
    async for event in runner.run_async(new_message=message_fallback, user_id="counselor_1", session_id="orch_session_high"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print("\n" + "-" * 60)

if __name__ == "__main__":
    asyncio.run(test_orchestrator())
