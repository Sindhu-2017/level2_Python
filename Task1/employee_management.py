# 9. Employee Management Console
# Maintain employee details using a collection.
# Menu:
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Find Highest Salary
# 5. Display Employees by Department
# 6. Exit
# Use:
# List 
# Dictionary 
# Loop 
# match-case 
# Conditions 
# Searching 
# Comprehension 

employees = []
while True :
    print ("1. Add Employee")
    print ("2. View Employees")
    print ("3. Search Employee")
    print ("4. Find Highest Salary")
    print ("5. Display Employees by Department")
    print ("6. Exit")
    choice = int (input ("Enter your choice :"))

    match choice :
        case 1:
            print ("1. Add Employee")
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))

            employee = {
                "name" : name,
                "department" : department ,
                "salary" : salary
            }   
            employees.append(employee)  
            print("Employee added successfully...")       
            
        case 2:
            if not employees :
                print("No employees found")
            else :
                for emp in employees :
                    print(f"Name : {emp['name']}")
                    print(f"Department : {emp['department']}")
                    print(f"Salary : {emp['salary']}")

        case 3:
            search_name = input("Enter employee name to search: ").lower()

            results = [ emp for emp in employees if emp["name"].lower() == search_name]
            if results:
                for emp in results:
                    print(emp)
            else:
                print("Employee not found")

        case 4:
            if employees:
                highest = 0
                for emp in employees :
                    if emp["salary"] > highest :
                        highest = emp["salary"]

                print("Highest salary :",highest)
            else:
                print("No employees available")

        case 5:
            department = input("Enter department: ").lower()
            results = [emp for emp in employees if emp["department"].lower() == department]
            if results:
                print(f"Employees in {department}")
                for emp in results:
                    print(emp)
            else:
                print("No employees found in this department.")
        case 6:
            print ("Exiting ... ")
            break
        case _:
            print("Invalid choice")