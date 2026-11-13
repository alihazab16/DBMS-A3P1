from datetime import date

from app.database import SessionLocal
from app.models import Student


def seedStudents():

    session = SessionLocal()

    try:

        # Initial student records
        students = [
            Student(
                first_name="John",
                last_name="Doe",
                email="john.doe@example.com",
                enrollment_date=date(2023, 9, 1)
            ),

            Student(
                first_name="Jane",
                last_name="Smith",
                email="jane.smith@example.com",
                enrollment_date=date(2023, 9, 1)
            ),

            Student(
                first_name="Jim",
                last_name="Beam",
                email="jim.beam@example.com",
                enrollment_date=date(2023, 9, 2)
            )
        ]

        # Check if the initial records already exist
        for student in students:

            existing = session.query(Student).filter_by(
                email=student.email
            ).first()

            if existing is None:
                session.add(student)

        # Save the records
        session.commit()

        print("Initial students inserted successfully!")

    except Exception as error:

        session.rollback()
        print("Error inserting initial students:", error)

    finally:
        session.close()


if __name__ == "__main__":
    seedStudents()