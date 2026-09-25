from dotenv import load_dotenv
import os
from utils.employee import *
from utils.salary import *
from utils.salary_report import *
from pathlib import Path

load_dotenv()
employee_file =Path(os.getenv("EMPLOYEE_FILE"))
salary_file = Path(os.getenv("SALARY_FILE"))

while True:
    print ("\n1-Display Employees")
    print ("2-Update Salary")
    print ("3-Display Employee with High Salary ")
    print ("4-Display Salary Report")
    print("5 -Check files exists or not")
    print ("6-Display File Information")
    print ("7-Exit")
    choice = input ("Enter your choice :")

    match choice :
        case "1":
            print ("1-Display Employees")
            employee_data=display_employees(employee_file)
            for employee in employee_data :
                print(f"ID : {employee["employee_id"]} - {employee["employee_name"]} - {employee["department"]} experience :{employee["experience"]}")


        case "2":
            print("2-Update Basic Salary")
            try:
                employee_id = int(input("Enter the Employee ID :"))
                updated_salary=float(input("Enter updated salary :"))
                update_salary(salary_file,employee_id,updated_salary)

            except ValueError:
                print("Enter valid numbers")

        case "3":
            print("3-Display Employee with High Salary")
            high_salary_employee = get_high_salary_employee(employee_file,salary_file)
            print(f"ID : {high_salary_employee['employee_id']} - {high_salary_employee['employee_name']} - {high_salary_employee['department']} experience :{high_salary_employee['experience']}")
            print(f"Basic Salary :{high_salary_employee["basic_salary"]}")
            print(f"HRA :{high_salary_employee["hra"]}")
            print(f"DA :{high_salary_employee["da"]}")
            print(f"Bonus :{high_salary_employee["bonus"]}")
            print(f"Net Salary :{high_salary_employee["net_salary"]}")

        case "4":
            print ("4-Display Salary Report")
            salary_report = display_salary_report(employee_file,salary_file)
            for report in salary_report:
                print(f"ID: {report["employee_id"]} -{report["employee_name"]} - {report["department"]} -experience :{report["experience"]}")
                print(f"Basic Salary :{report["basic_salary"]}")
                print(f"HRA :{report["hra"]}")
                print(f"DA :{report["da"]}")
                print(f"Bonus :{report["bonus"]}")
                print(f"Net Salary :{report["net_salary"]}")

                print("_" * 40)

        case "5":
            print("5 -Check files exists or not")
            if employee_file.exists():
                print("Employee file exists")
            else:
                print("Employee file does not exists")

            if salary_file.exists():
                print("Salary file exists")
            else:
                print("Salary file does not exists")

        case "6":
            print ("6-Display File Information")
            print ("Employee File Details :")
            print("_" * 40)
            print(f"File Name : {employee_file.name}")
            print(f"Parent : {employee_file.parent}")
            print(f"Suffix : {employee_file.suffix}")
            print(f"Full Path : {employee_file.resolve()}")

            print ("Salary File Details :")
            print("_" * 40)
            print(f"File Name : {salary_file.name}")
            print(f"Parent : {salary_file.parent}")
            print(f"Suffix : {salary_file.suffix}")
            print(f"Full Path : {salary_file.resolve()}")


        case "7":
            print("Exiting...")
            break

        case _:
            print("Invalid choice")
