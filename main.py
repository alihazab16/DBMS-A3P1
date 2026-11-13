from datetime import datetime

from app.students import (
    getAllStudents,
    addStudent,
    updateStudentEmail,
    deleteStudent
)


def main():

    while True:

        print("\n===== STUDENT DATABASE =====")

        print("1. Display all students")
        print("2. Add a student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # Display all students
        if choice == "1":

            getAllStudents()

        # Add a student
        elif choice == "2":

            first_name = input("Enter first name: ")

            last_name = input("Enter last name: ")

            email = input("Enter email: ")

            enrollment = input(
                "Enter enrollment date (YYYY-MM-DD), or leave empty: "
            )

            if enrollment.strip():
                enrollment_date = datetime.strptime(
                    enrollment, "%Y-%m-%d"
                ).date()
            else:
                enrollment_date = None

            addStudent(
                first_name,
                last_name,
                email,
                enrollment_date
            )

        # Update student email
        elif choice == "3":

            student_id = int(input("Enter student ID: "))

            new_email = input("Enter new email: ")

            updateStudentEmail(student_id, new_email)

        # Delete a student
        elif choice == "4":

            student_id = int(input("Enter student ID: "))

            deleteStudent(student_id)

        # Exit
        elif choice == "5":

            print("Goodbye!")
            break

        else:

            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()