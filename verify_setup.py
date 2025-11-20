import sys
import os
from datetime import date

# Add the current directory to sys.path
sys.path.append(os.getcwd())

from school_dropout_agent.core.domain.student import Student
from school_dropout_agent.infrastructure.database.database import init_db, SessionLocal
from school_dropout_agent.infrastructure.database.models import StudentModel

def main():
    print("Verifying setup...")
    
    # 1. Verify Domain Entities
    try:
        s = Student(
            student_id="123",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            enrollment_status="Active",
            major="CS",
            enrollment_date=date.today()
        )
        print(f"Domain Entity created: {s}")
    except Exception as e:
        print(f"Failed to create Domain Entity: {e}")
        return

    # 2. Verify Database
    print("Initializing database...")
    try:
        init_db()
        print("Database initialized.")
    except Exception as e:
        print(f"Failed to initialize database: {e}")
        return
    
    db = SessionLocal()
    try:
        # Check if exists
        existing = db.query(StudentModel).filter_by(student_id="123").first()
        if not existing:
            student_model = StudentModel(
                student_id="123",
                first_name="John",
                last_name="Doe",
                email="john@example.com",
                enrollment_status="Active",
                major="CS",
                enrollment_date=datetime.now()
            )
            db.add(student_model)
            db.commit()
            print("Student added to DB.")
        else:
            print("Student already in DB.")
            
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        db.close()

    print("Verification complete.")

if __name__ == "__main__":
    from datetime import datetime
    main()
