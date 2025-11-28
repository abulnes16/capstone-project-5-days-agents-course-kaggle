"""
Entry point for ADK web interface.
This file is automatically loaded by `adk web` command.
"""
from school_dropout_agent.agents.orchestrator.agent import DropoutPreventionOrchestrator
from school_dropout_agent.infrastructure.memory.database_memory import DatabaseMemoryService
from school_dropout_agent.infrastructure.database.database import init_db

# Initialize database
init_db()

# Create memory service
memory_service = DatabaseMemoryService()

# Create root agent with memory service
root_agent = DropoutPreventionOrchestrator(memory_service=memory_service)
