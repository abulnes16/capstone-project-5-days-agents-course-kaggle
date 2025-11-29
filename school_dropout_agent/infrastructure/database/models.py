"""
This module defines the SQLAlchemy database models.
It maps the domain entities (Student, RiskProfile, Intervention) to database tables.
Used by the DatabaseMemoryService for persistence.
"""
from sqlalchemy import Column, String, Float, DateTime, Integer, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from school_dropout_agent.core.domain.intervention import InterventionStatus, InterventionType

Base = declarative_base()

class StudentModel(Base):
    __tablename__ = "students"
    
    student_id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    enrollment_status = Column(String)
    major = Column(String)
    enrollment_date = Column(DateTime)
    metadata_json = Column(JSON)

class RiskProfileModel(Base):
    __tablename__ = "risk_profiles"
    
    student_id = Column(String, ForeignKey("students.student_id"), primary_key=True)
    risk_score = Column(Float)
    risk_level = Column(String)
    last_updated = Column(DateTime)
    risk_factors = Column(JSON)
    
    student = relationship("StudentModel", backref="risk_profile")

class InterventionModel(Base):
    __tablename__ = "interventions"
    
    intervention_id = Column(String, primary_key=True)
    student_id = Column(String, ForeignKey("students.student_id"))
    type = Column(SQLEnum(InterventionType))
    status = Column(SQLEnum(InterventionStatus))
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    student = relationship("StudentModel", backref="interventions")

class EventModel(Base):
    __tablename__ = "events"
    
    event_id = Column(String, primary_key=True)
    event_type = Column(String)
    timestamp = Column(DateTime)
    payload = Column(JSON)
    source = Column(String)
