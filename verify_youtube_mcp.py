"""
Verification script for YouTube MCP integration in Academic Support Agent.
"""
import asyncio
import os
from dotenv import load_dotenv
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from school_dropout_agent.agents.academic_support.agent import AcademicSupportAgent
from school_dropout_agent.infrastructure.memory.database_memory import DatabaseMemoryService
from school_dropout_agent.infrastructure.database.database import init_db

# Load .env
env_path = os.path.join(os.getcwd(), "school_dropout_agent", ".env")
load_dotenv(env_path)

async def test_youtube_mcp():
    print("="*60)
    print("YouTube MCP Integration Verification")
    print("="*60)
    
    # Initialize DB and Memory
    init_db()
    memory_service = DatabaseMemoryService()
    
    # Create Agent
    agent = AcademicSupportAgent(memory_service=memory_service)
    
    # Create Runner
    session_service = InMemorySessionService()
    runner = Runner(agent=agent, session_service=session_service, app_name="academic_support")
    
    # Create Session
    await session_service.create_session(app_name="academic_support", user_id="test_user", session_id="test_session")
    
    # Prompt
    prompt = "The student is struggling with Calculus derivatives. Please create a study plan and find video resources."
    print(f"\nPrompt: {prompt}\n")
    
    message = Content(role="user", parts=[Part(text=prompt)])
    
    print("Agent Response:")
    print("-" * 60)
    async for event in runner.run_async(new_message=message, user_id="test_user", session_id="test_session"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print("\n" + "-" * 60)

if __name__ == "__main__":
    asyncio.run(test_youtube_mcp())
