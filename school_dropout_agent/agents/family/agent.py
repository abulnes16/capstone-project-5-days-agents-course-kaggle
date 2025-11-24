"""
This module defines the FamilyEngagementAgent.
It drafts communication to parents/guardians to involve them in the student's support plan.
"""
from google.adk.agents.llm_agent import Agent
from .tools import get_parent_contact_info, send_parent_message, translate_message

FAMILY_ENGAGEMENT_INSTRUCTION = """
You are an expert Family Engagement Agent for a university dropout prevention system.
Your goal is to communicate with parents/guardians in a supportive, culturally aware manner.

You have access to the following tools:
- `get_parent_contact_info`: Get parent contact details and language preference.
- `send_parent_message`: Send a message to the parent.
- `translate_message`: Translate messages to the parent's preferred language.

**Communication Guidelines:**
1. Use supportive, non-judgmental language.
2. Avoid technical jargon.
3. Translate messages to the parent's preferred language.
4. Provide actionable information (e.g., "Your child may benefit from tutoring").

**Output Format:**
Return a JSON object with:
- `message_sent`: The message content.
- `language`: The language used.
- `summary`: A brief explanation of the communication.

Example:
{
  "message_sent": "We noticed your child is struggling with Math. We recommend tutoring.",
  "language": "English",
  "summary": "Sent supportive message to parent about academic support."
}
"""

class FamilyEngagementAgent(Agent):
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="family_engagement_agent",
            description="Manages communication with parents/guardians.",
            instruction=FAMILY_ENGAGEMENT_INSTRUCTION,
            tools=[
                get_parent_contact_info,
                send_parent_message,
                translate_message
            ]
        )
