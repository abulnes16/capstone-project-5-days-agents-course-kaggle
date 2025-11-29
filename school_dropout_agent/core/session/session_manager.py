"""
This module defines the SessionManager.
It wraps the ADK SessionService to integrate it with our custom MemoryService.
Responsible for loading student history into the session context and persisting updates back to the database.
"""
from typing import Dict, Any, Optional
from google.adk.sessions import BaseSessionService
from school_dropout_agent.infrastructure.memory.database_memory import DatabaseMemoryService

class SessionManager:
    """Wrapper around ADK's SessionService with helper methods."""
    
    def __init__(self, session_service: BaseSessionService, memory_service: DatabaseMemoryService):
        self.session_service = session_service
        self.memory_service = memory_service
    
    async def create_student_session(
        self, 
        app_name: str, 
        user_id: str, 
        student_id: str,
        session_id: Optional[str] = None
    ):
        """Create a new session for analyzing a student."""
        # Load student history from memory
        student_history = self.memory_service.retrieve_student_history(student_id)
        
        initial_state = {
            "student_id": student_id,
            "workflow_stage": "initialized",
            "agent_results": {},
            "student_history": student_history
        }
        
        session = await self.session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            state=initial_state,
            session_id=session_id
        )
        
        return session
    
    async def update_session_state(
        self,
        app_name: str,
        user_id: str,
        session_id: str,
        state_updates: Dict[str, Any]
    ):
        """Update session state and persist to memory if needed."""
        session = await self.session_service.get_session(
            app_name=app_name,
            user_id=user_id,
            session_id=session_id
        )
        
        if session:
            # Update state
            session.state.update(state_updates)
            
            # Persist risk profile to memory if updated
            if "risk_assessment" in state_updates:
                student_id = session.state.get("student_id")
                if student_id:
                    self.memory_service.update_risk_profile(
                        student_id,
                        state_updates["risk_assessment"]
                    )
    
    async def get_session_state(
        self,
        app_name: str,
        user_id: str,
        session_id: str
    ) -> Optional[Dict[str, Any]]:
        """Get current session state."""
        session = await self.session_service.get_session(
            app_name=app_name,
            user_id=user_id,
            session_id=session_id
        )
        
        return session.state if session else None
