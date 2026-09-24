# 10. Student Management Console ⭐⭐⭐
# Menu:
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Calculate Average
# 5. Find Topper
# 6. Display Passed Students
# 7. Exit
# Use a list of dictionaries.
# Example:
# students = [
#     {"name": "Arun", "mark": 85},
#     {"name": "Priya", "mark": 92},
#     {"name": "Kumar", "mark": 67}
# ]

students = [
    {"name": "Arun", "mark": 85},
    {"name": "Priya", "mark": 92},
    {"name": "Kumar", "mark": 67}
]
while True :
    print ("1. Add Student")
    print ("2. View Students")
    print ("3. Search Student")
    print ("4. Calculate Average")
    print ("5. Find Topper")
    print ("6. Display Passed Students")
    print ("7. Exit")
    choice = int (input ("Enter your choice :"))

    match choice :
        case 1:
            print ("1. Add Student")
            name = input("Enter Student name: ")
            mark = float(input("Enter mark: "))

            if 0 <= mark <= 100:
                students.append({"name": name, "mark": mark})
                print("Student added successfully.")
            else:
                print("Invalid mark. Enter a value from 0 to 100.")      
            
        case 2:
            if students:
                for student in students:
                    print(f"Name: {student['name']}, "f"Mark: {student['mark']}")
            else:
                print("No students found.")

        case 3:
            name = input("Enter student name to search: ").lower()

            result = [student for student in students if student["name"].lower() == name]

            if result:
                print(result[0])
            else:
                print("Student not found.")

        case 4:
            if students:
                average = sum(student["mark"] for student in students) / len(students)
                print(f"Average Mark: {average}")
            else:
                print("No students available.")

        case 5:
            if students:
                topper =students[0]
                for student in students :
                    if student["mark"] > topper["mark"]:
                        topper = student
                print("Topper:",topper)

            else:
                print("No students available.")

        case 6:
            passed = [student for student in students if student["mark"] >= 40]
            if passed:
                print("Passed Students:")
                for student in passed:
                    print(student)
            else:
                print("No passed students.")

        case 7:
            print ("Exiting ... ")
            break
        case _:
            print("Invalid choice")