import sys
import os
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.getcwd())

# Load .env from school_dropout_agent/.env
env_path = os.path.join(os.getcwd(), "school_dropout_agent", ".env")
load_dotenv(env_path)

APP_NAME = "risk_prediction"

import asyncio
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from school_dropout_agent.agents.risk_prediction.agent import RiskPredictionAgent

async def main():
    print("Initializing Risk Prediction Agent...")
    agent = RiskPredictionAgent()

    service_session = InMemorySessionService()
    await service_session.create_session(app_name=APP_NAME, user_id="user_1", session_id="session_1")
    
    runner = Runner(agent=agent, session_service=service_session, app_name=APP_NAME)
    
    student_id = "risk_case_1"
    print(f"Analyzing student: {student_id}")
    
    prompt = f"Analyze the risk profile for student_id: {student_id}"
    message = Content(role="user", parts=[Part(text=prompt)])
    
    print("\nAgent Response:")
    async for event in runner.run_async(new_message=message, user_id="user_1", session_id="session_1"):
        if hasattr(event, 'content') and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
        elif hasattr(event, 'part') and event.part and hasattr(event.part, 'text') and event.part.text:
             print(event.part.text, end="", flush=True)
        elif hasattr(event, 'text') and event.text:
             print(event.text, end="", flush=True)
             
    print("\n")

if __name__ == "__main__":
    asyncio.run(main())
