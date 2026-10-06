import csv
students=[]
with open("students.csv") as file:
    reader = csv.DictReader(file)
    print("Student list:")

    for student in reader:
        students.append(student)
        print(student)

def add_student(students):
    roll=input("Roll Number: ").upper()
    name=input("Name: ")
    marks=input("Marks: ")

    student={
        "roll":roll,
        "name":name,
        "marks":marks
    }
    students.append(student)
    save_students(students)

    print("student successfully added")

def save_students(students):
    with open("students.csv", "w", newline="") as file:
        fieldnames = ["roll", "name", "marks"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

def search_student(students):
    roll = input("Enter roll number to search: ").upper()

    for student in students:
        if student["roll"] == roll:
            print("Student found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")
def delete_student(students):
    roll = input("Enter roll number to delete: ").upper()
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student successfully deleted")
            return

    print("Student not found.")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        search_student(students)

    elif choice == "3":
        delete_student(students)

    elif choice == "4":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice.")