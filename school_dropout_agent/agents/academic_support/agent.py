"""
This module defines the AcademicSupportAgent.
It creates personalized study plans based on the student's academic performance and learning style.
"""
from google.adk.agents.llm_agent import Agent
from .tools import get_weak_subjects, get_learning_style, get_study_resources

ACADEMIC_SUPPORT_INSTRUCTION = """
You are an expert Academic Support Agent for a university dropout prevention system.
Your goal is to create personalized study plans and recommend resources for struggling students.

You have access to the following tools:
- `get_weak_subjects`: Identify subjects where the student is struggling.
- `get_learning_style`: Get the student's preferred learning style.
- `get_study_resources`: Fetch relevant study resources for specific topics.

**Your Task:**
1. Identify the student's weak subjects.
2. Understand their learning style preferences.
3. Recommend tailored study resources for each weak subject.
    
**Output Format:**
}
"""


from school_dropout_agent.agents.orchestrator.tools import save_agent_result

class AcademicSupportAgent(Agent):
    def __init__(self, memory_service=None, model_name: str = "gemini-2.5-flash"):
        super().__init__(
            model=model_name,
            name="academic_support_agent",
            description="Generates personalized study plans and resources.",
            instruction=ACADEMIC_SUPPORT_INSTRUCTION,
            tools=[
                get_weak_subjects,
                get_learning_style,
                get_study_resources,
                save_agent_result
            ]
        )
        object.__setattr__(self, 'memory_service', memory_service)

