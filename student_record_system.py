# Student Record Management System

students = []


# -------------------- FUNCTION TO CALCULATE GRADE --------------------
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# -------------------- ADD STUDENT --------------------
def add_student():
    roll = input("Enter Roll Number: ")

    # Prevent duplicate roll numbers (Bonus Feature)
    for student in students:
        if student["roll"] == roll:
            print("Roll Number already exists!")
            return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


# -------------------- VIEW ALL STUDENTS --------------------
def view_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    for student in students:
        print("---------------------------------")
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
    print("---------------------------------\n")


# -------------------- SEARCH STUDENT --------------------
def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            print()
            return

    print("Student not found.\n")


# -------------------- CLASS STATISTICS --------------------
def class_statistics():
    if len(students) == 0:
        print("No data available.\n")
        return

    total_students = len(students)
    total_average = 0

    highest = students[0]
    lowest = students[0]

    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for student in students:
        total_average += student["average"]

        if student["total"] > highest["total"]:
            highest = student

        if student["total"] < lowest["total"]:
            lowest = student

        grade_count[student["grade"]] += 1

    class_avg = total_average / total_students

    print("\n------ CLASS STATISTICS ------")
    print("Total Students:", total_students)
    print("Class Average:", round(class_avg, 2))
    print("Highest Scorer:", highest["name"], "-", highest["total"])
    print("Lowest Scorer:", lowest["name"], "-", lowest["total"])

    print("\nGrade Distribution:")
    for grade in grade_count:
        print(grade, ":", grade_count[grade])
    print()


# -------------------- MAIN MENU --------------------
def main():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Class Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run Program
main()