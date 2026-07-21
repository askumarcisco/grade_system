class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("-" * 50)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Marks      : {self.marks}")
        print(f"Average    : {self.average():.2f}")
        print(f"Grade      : {self.grade()}")
        print("-" * 50)


students = {}


def add_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter Mark {i}: "))
        marks.append(mark)

    students[student_id] = Student(student_id, name, marks)
    print("Student added successfully.\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    for student in students.values():
        student.display()


def search_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        students[student_id].display()
    else:
        print("Student not found.\n")


def update_student():
    student_id = input("Enter Student ID to update: ")

    if student_id not in students:
        print("Student not found.\n")
        return

    name = input("Enter New Name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter New Mark {i}: "))
        marks.append(mark)

    students[student_id] = Student(student_id, name, marks)
    print("Student updated successfully.\n")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")


def topper():
    if not students:
        print("No records found.\n")
        return

    top = max(students.values(), key=lambda s: s.average())

    print("\nTopper Details")
    top.display()


def menu():
    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            topper()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()