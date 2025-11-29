"""
This module implements the DatabaseMemoryService.
It provides the concrete logic for storing and retrieving data using SQLAlchemy.
Acts as the bridge between the application core and the database.
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
import json
from school_dropout_agent.core.memory.memory_service import MemoryService
from school_dropout_agent.infrastructure.database.database import SessionLocal
from school_dropout_agent.infrastructure.database.models import (
    StudentModel, RiskProfileModel, InterventionModel
)
from school_dropout_agent.core.domain.intervention import InterventionType, InterventionStatus

class DatabaseMemoryService(MemoryService):
    """Memory service using PostgreSQL/SQLite database."""
    
    def store_student_profile(self, student_id: str, profile_data: Dict[str, Any]) -> None:
        """Store or update a student's profile."""
        db = SessionLocal()
        try:
            student = db.query(StudentModel).filter_by(student_id=student_id).first()
            if student:
                # Update existing
                for key, value in profile_data.items():
                    if hasattr(student, key):
                        setattr(student, key, value)
            else:
                # Create new
                student = StudentModel(student_id=student_id, **profile_data)
                db.add(student)
            db.commit()
        finally:
            db.close()
    
    def retrieve_student_history(self, student_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a student's complete history."""
        db = SessionLocal()
        try:
            student = db.query(StudentModel).filter_by(student_id=student_id).first()
            if not student:
                return None
            
            # Get risk profile
            risk_profile = db.query(RiskProfileModel).filter_by(student_id=student_id).first()
            
            # Get interventions
            interventions = db.query(InterventionModel).filter_by(student_id=student_id).all()
            
            return {
                "student_id": student.student_id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "enrollment_status": student.enrollment_status,
                "major": student.major,
                "enrollment_date": student.enrollment_date.isoformat() if student.enrollment_date else None,
                "risk_profile": {
                    "risk_score": risk_profile.risk_score,
                    "risk_level": risk_profile.risk_level,
                    "last_updated": risk_profile.last_updated.isoformat() if risk_profile.last_updated else None,
                    "risk_factors": risk_profile.risk_factors
                } if risk_profile else None,
                "interventions": [
                    {
                        "intervention_id": i.intervention_id,
                        "type": i.type.value if hasattr(i.type, 'value') else str(i.type),
                        "status": i.status.value if hasattr(i.status, 'value') else str(i.status),
                        "description": i.description,
                        "created_at": i.created_at.isoformat() if i.created_at else None
                    } for i in interventions
                ]
            }
        finally:
            db.close()
    
    def update_risk_profile(self, student_id: str, risk_data: Dict[str, Any]) -> None:
        """Update a student's risk assessment."""
        db = SessionLocal()
        try:
            risk_profile = db.query(RiskProfileModel).filter_by(student_id=student_id).first()
            if risk_profile:
                risk_profile.risk_score = risk_data.get("risk_score", risk_profile.risk_score)
                risk_profile.risk_level = risk_data.get("risk_level", risk_profile.risk_level)
                risk_profile.risk_factors = risk_data.get("risk_factors", risk_profile.risk_factors)
                risk_profile.last_updated = datetime.now()
            else:
                risk_profile = RiskProfileModel(
                    student_id=student_id,
                    risk_score=risk_data.get("risk_score", 0.0),
                    risk_level=risk_data.get("risk_level", "Low"),
                    risk_factors=risk_data.get("risk_factors", []),
                    last_updated=datetime.now()
                )
                db.add(risk_profile)
            db.commit()
        finally:
            db.close()
    
    def store_intervention(self, student_id: str, intervention_data: Dict[str, Any]) -> str:
        """Store an intervention and return its ID."""
        db = SessionLocal()
        try:
            intervention_type = intervention_data.get("type", "Academic")
            if isinstance(intervention_type, str):
                intervention_type = InterventionType[intervention_type.upper()]
            
            intervention = InterventionModel(
                intervention_id=intervention_data.get("intervention_id"),
                student_id=student_id,
                type=intervention_type,
                status=InterventionStatus.PENDING,
                description=intervention_data.get("description", ""),
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.add(intervention)
            db.commit()
            return intervention.intervention_id
        finally:
            db.close()
    
    def get_interventions(self, student_id: str) -> List[Dict[str, Any]]:
        """Get all interventions for a student."""
        db = SessionLocal()
        try:
            interventions = db.query(InterventionModel).filter_by(student_id=student_id).all()
            return [
                {
                    "intervention_id": i.intervention_id,
                    "type": i.type.value if hasattr(i.type, 'value') else str(i.type),
                    "status": i.status.value if hasattr(i.status, 'value') else str(i.status),
                    "description": i.description,
                    "created_at": i.created_at.isoformat() if i.created_at else None
                } for i in interventions
            ]
        finally:
            db.close()
