"""
This module defines the EmotionalBehavioralAgent.
It analyzes qualitative data (counseling notes, surveys) to assess the student's emotional well-being.
"""
from google.adk.agents.llm_agent import Agent
from .tools import get_counseling_visits, get_survey_responses, get_social_engagement

EMOTIONAL_AGENT_INSTRUCTION = """
You are an expert Emotional & Behavioral Agent for a university dropout prevention system.
Your goal is to analyze a student's emotional and behavioral patterns to identify signs of distress.

You have access to the following tools:
- `get_counseling_visits`: Check counseling visit history.
- `get_survey_responses`: Check recent survey responses and sentiment.
- `get_social_engagement`: Check campus and social engagement levels.

**Behavioral Flags to Look For:**
1. Increased counseling visits (>3 in last 30 days).
2. High stress levels (>4 out of 5).
3. Low satisfaction scores (<3 out of 5).
4. Declining social engagement (no club memberships, low event attendance).
5. Negative sentiment in survey comments.

**Output Format:**
1. Call `save_agent_result` with the full JSON analysis.
2. Return a BRIEF 1-sentence summary (e.g., "Detected high stress and low satisfaction.").
"""


from school_dropout_agent.agents.orchestrator.tools import save_agent_result

class EmotionalBehavioralAgent(Agent):
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="emotional_behavioral_agent",
            description="Analyzes student emotional and behavioral patterns.",
            instruction=EMOTIONAL_AGENT_INSTRUCTION,
            tools=[
                get_counseling_visits,
                get_survey_responses,
                get_social_engagement,
                save_agent_result
            ]
        )
        object.__setattr__(self, 'memory_service', memory_service)
