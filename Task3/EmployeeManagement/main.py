from dotenv import load_dotenv
import os
from utils.employee import *
from utils.salary import *
from utils.salary_report import *
from utils.analytics import *
from pathlib import Path
from datetime import date

load_dotenv()

employee_file =Path(os.getenv("EMPLOYEE_FILE"))
salary_file = Path(os.getenv("SALARY_FILE"))

while True:

    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1.Display Employees")
    print("2.Add New Salary Record")
    print("3.Display Highest Salary Employee")
    print("4.Display Salary Report")
    print("5.Display Departments")
    print("6.Sort Employees by Salary")
    print("7.Sort Employees by Experience")
    print("8.Search Employees by Department")
    print("9.Display Experienced Employees")
    print("10.Display Average Salary")
    print("11.Check Salary Condition")
    print("12.Check Files Exists")
    print("13.Display File Information")
    print("14.Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":

            employees = display_employees(employee_file)

            if employees:
                display_employee_list(employees)
            else:
                print("No employee records found.")

        case "2":

            try:
                employee_id = int(input("Enter employee ID: "))
                basic_salary = float(input("Enter basic salary: "))
                experience = int(input("Enter experience: "))

                hra = calculate_hra(basic_salary)
                da = calculate_da(basic_salary)
                bonus = calculate_bonus(basic_salary, experience)
                net_salary = calculate_netsalary(basic_salary, experience)

                updated_date = date.today().isoformat()

                new_salary_data = {
                    "employee_id": employee_id,
                    "basic_salary": basic_salary,
                    "hra": hra,
                    "da": da,
                    "bonus": bonus,
                    "net_salary": net_salary,
                    "updated_date": updated_date
                }

                add_salary(salary_file, new_salary_data)

                print(f"HRA : {hra}")
                print(f"DA : {da}")
                print(f"Bonus : {bonus}")
                print(f"Net Salary : {net_salary}")

            except ValueError:
                print("Enter valid numbers.")

        case "3":

            employees = display_salary_report(
                employee_file,
                salary_file
            )

            high_salary_employee = get_highest_salary_employee(
                employees
            )

            if high_salary_employee:

                print(
                    f"ID : {high_salary_employee['employee_id']} - "
                    f"{high_salary_employee['employee_name']}"
                )

                print(
                    f"Department : "
                    f"{high_salary_employee['department']}"
                )

                print(
                    f"Basic Salary : "
                    f"{high_salary_employee['basic_salary']}"
                )

                print(
                    f"Net Salary : "
                    f"{high_salary_employee['net_salary']}"
                )

            else:
                print("No salary records found.")

        case "4":

            reports = display_salary_report(
                employee_file,
                salary_file
            )

            if reports:

                for number, report in enumerate(
                    reports,
                    start=1
                ):

                    print(
                        f"\n{number}. "
                        f"ID: {report['employee_id']} - "
                        f"{report['employee_name']} - "
                        f"{report['department']}"
                    )

                    print(
                        f"Designation : "
                        f"{report['designation']}"
                    )

                    print(
                        f"Experience : "
                        f"{report['experience']}"
                    )

                    print(
                        f"Basic Salary : "
                        f"{report['basic_salary']}"
                    )

                    print(
                        f"HRA : {report['hra']}"
                    )

                    print(
                        f"DA : {report['da']}"
                    )

                    print(
                        f"Bonus : {report['bonus']}"
                    )

                    print(
                        f"Net Salary : "
                        f"{report['net_salary']}"
                    )

                    print(
                        f"Updated Date : "
                        f"{report['updated_date']}"
                    )

                    print("_" * 40)

            else:
                print("No salary records found.")

        case "5":

            employees = display_salary_report(
                employee_file,
                salary_file
            )

            departments = get_departments(
                employees
            )

            for department in departments:
                print(department)

        case "6":

            employees = display_salary_report(
                employee_file,
                salary_file
            )

            sorted_employees = sort_by_salary(
                employees
            )

            display_employee_list(
                sorted_employees
            )

        case "7":

            employees = display_salary_report(
                employee_file,
                salary_file
            )

            sorted_employees = sort_by_experience(
                employees
            )

            display_employee_list(
                sorted_employees
            )

        case "8":

            department = input(
                "Enter department: "
            )

            employees = display_salary_report(
                employee_file,
                salary_file
            )

            result = get_department_employees(
                employees,
                department
            )

            if result:
                display_employee_list(result)
            else:
                print("No employees found.")

        case "9":

            try:

                minimum_experience = int(
                    input("Enter minimum experience: ")
                )

                employees = display_salary_report(
                    employee_file,
                    salary_file
                )

                result = get_experienced_employees(
                    employees,
                    minimum_experience
                )

                if result:
                    display_employee_list(result)
                else:
                    print("No employees found.")

            except ValueError:
                print("Enter valid experience.")

        case "10":

            employees = display_salary_report(
                employee_file,
                salary_file
            )

            average_salary = calculate_average_salary(
                employees
            )

            print(
                f"Average Salary : "
                f"{average_salary:.2f}"
            )

        case "11":

            employees = display_salary_report(
                employee_file,
                salary_file
            )

            check_salary_condition(
                employees
            )

        case "12":

            if employee_file.exists():
                print("Employee file exists.")
            else:
                print("Employee file does not exist.")

            if salary_file.exists():
                print("Salary file exists.")
            else:
                print("Salary file does not exist.")

        case "13":

            print("\nEmployee File Information")
            print("_" * 30)
            print(f"File Name : {employee_file.name}")
            print(f"Parent : {employee_file.parent}")
            print(f"Suffix : {employee_file.suffix}")
            print(f"Full Path : {employee_file.resolve()}")

            print("\nSalary File Information")
            print("_" * 30)
            print(f"File Name : {salary_file.name}")
            print(f"Parent : {salary_file.parent}")
            print(f"Suffix : {salary_file.suffix}")
            print(f"Full Path : {salary_file.resolve()}")

        case "14":

            print("Exiting...")
            break

        case _:

            print("Invalid choice.")