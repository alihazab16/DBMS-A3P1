from sqlalchemy import select,insert,delete,update
from app.database import SessionLocal
from app.models import Student


def getAllStudents():
    session = SessionLocal()
    try:

        
        statement = select(Student)

        # Execute the query and retrieve all students
        students = session.scalars(statement).all()

        # Display each student
        for student in students:
            print(
                student.student_id,
                student.first_name,
                student.last_name,
                student.email,
                student.enrollment_date
            )

        return students

    finally:
        session.close()

def addStudent(first_name, last_name, email, enrollment_date):
    session = SessionLocal()
    try:
        new_student = Student(
        first_name="Ali",
        last_name="Azab",
        email="ali@example.com",
        enrollment_date=None
    )

        session.add(new_student)
        session.commit()
        print("Student added successfully!")
        return new_student

    except Exception as error:

        # Undo changes if something goes wrong
        session.rollback()

        print("Error adding student:", error)

        return None

    finally:
        session.close()


def updateStudentEmail(student_id, new_email):

    session = SessionLocal()

    try:

        # Find the student using their primary key
        student = session.get(Student, student_id)

        # Check if the student exists
        if student is None:
            print("Student not found.")
            return False

        # Update the email
        student.email = new_email

        session.commit()

        print("Student email updated successfully!")

        return True

    except Exception as error:

        
        session.rollback()

        print("Error updating student:", error)

        return False

    finally:
        session.close()

def deleteStudent(student_id):
    session = SessionLocal()

    try:
        student = session.get(Student, student_id)
        if student is None:
            print("Student not found")
            return False

        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
        return True

    except Exception as error:
        session.rollback()
        print("Error deleting Student:", error)
        return False

    finally:
        session.close()

