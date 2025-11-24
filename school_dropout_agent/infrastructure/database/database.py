"""
This module handles database connection and session management.
It provides the `get_db` context manager and initializes the database engine.
Defaults to SQLite for local development but supports PostgreSQL.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os

# Default to SQLite for local dev if no URL provided
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./school_dropout_agent.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
