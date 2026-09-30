from dotenv import load_dotenv
import os
from pathlib import Path
from datetime import date

from utils.employee import get_employees

from utils.salary import (
    calculate_hra,
    calculate_da,
    calculate_bonus,
    calculate_net_salary,
    add_salary
)

from utils.salary_report import get_report

from utils.analytics import (
    display_employees,
    get_highest_salary_employee,
    get_departments,
    sort_by_salary,
    sort_by_experience,
    get_department_employees,
    get_experienced_employees,
    calculate_average_salary,
    check_salary_condition
)


load_dotenv()

employee_file: Path = Path(
    os.getenv("EMPLOYEE_FILE", "")
)

salary_file: Path = Path(
    os.getenv("SALARY_FILE", "")
)


while True:

    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. Display Employees")
    print("2. Add New Salary Record")
    print("3. Display Highest Salary Employee")
    print("4. Display Salary Report")
    print("5. Display Departments")
    print("6. Sort Employees by Salary")
    print("7. Sort Employees by Experience")
    print("8. Search Employees by Department")
    print("9. Display Experienced Employees")
    print("10. Display Average Salary")
    print("11. Check Salary Condition")
    print("12. Exit")

    choice: str = input("Enter your choice: ")

    match choice:

        case "1":

            employees: list[dict] = get_employees(
                employee_file
            )

            if employees:
                display_employees(employees)
            else:
                print("No employee records found.")

        case "2":

            try:

                employee_id: int = int(
                    input("Enter employee ID: ")
                )

                employees: list[dict] = get_employees(
                    employee_file
                )

                if not any(
                    employee["employee_id"] == employee_id
                    for employee in employees
                ):
                    print("Employee ID does not exist.")
                    continue

                basic_salary: float = float(
                    input("Enter basic salary: ")
                )

                hra: float = calculate_hra(basic_salary)
                da: float = calculate_da(basic_salary)
                bonus: float = calculate_bonus(basic_salary)

                net_salary: float = calculate_net_salary(
                    basic_salary,
                    hra,
                    da,
                    bonus
                )

                updated_date: str = date.today().isoformat()

                new_salary_data: dict = {
                    "employee_id": employee_id,
                    "basic_salary": basic_salary,
                    "hra": hra,
                    "da": da,
                    "bonus": bonus,
                    "net_salary": net_salary,
                    "updated_date": updated_date
                }

                add_salary(
                    salary_file,
                    new_salary_data
                )

                print(f"HRA : {hra}")
                print(f"DA : {da}")
                print(f"Bonus : {bonus}")
                print(f"Net Salary : {net_salary}")

            except ValueError:

                print("Enter valid numbers.")

        case "3":

            employees: list[dict] = get_report(
                employee_file,
                salary_file
            )

            employee: dict | None = get_highest_salary_employee(
                employees
            )

            if employee:

                print(
                    f"Name : "
                    f"{employee['employee_name']}"
                )

                print(
                    f"Department : "
                    f"{employee['department']}"
                )

                print(
                    f"Salary : "
                    f"{employee['net_salary']}"
                )

            else:
                print("No salary records found.")

        case "4":

            reports: list[dict] = get_report(
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
                        f"ID : {report['employee_id']} - "
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
                        f"HRA : "
                        f"{report['hra']}"
                    )

                    print(
                        f"DA : "
                        f"{report['da']}"
                    )

                    print(
                        f"Bonus : "
                        f"{report['bonus']}"
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
                print("No salary records found")

        case "5":

            employees: list[dict] = get_report(
                employee_file,
                salary_file
            )

            departments: set[str] = get_departments(
                employees
            )

            for department in departments:
                print(department)

        case "6":

            employees: list[dict] = get_report(
                employee_file,
                salary_file
            )

            sorted_employees: list[dict] = sort_by_salary(
                employees
            )

            display_employees(
                sorted_employees
            )

        case "7":

            employees: list[dict] = get_report(
                employee_file,
                salary_file
            )

            sorted_employees: list[dict] = sort_by_experience(
                employees
            )

            display_employees(
                sorted_employees
            )

        case "8":

            department: str = input(
                "Enter department: "
            )

            employees: list[dict] = get_report(
                employee_file,
                salary_file
            )

            result: list[dict] = get_department_employees(
                employees,
                department
            )

            if result:
                display_employees(result)
            else:
                print("No employees found.")

        case "9":

            try:

                minimum_experience: int = int(
                    input(
                        "Enter minimum experience: "
                    )
                )

                employees: list[dict] = get_report(
                    employee_file,
                    salary_file
                )

                result: list[dict] = get_experienced_employees(
                    employees,
                    minimum_experience
                )

                if result:
                    display_employees(result)
                else:
                    print("No employees found.")

            except ValueError:
                print("Enter valid experience.")

        case "10":

            employees: list[dict] = get_report(
                employee_file,
                salary_file
            )

            average_salary: float = calculate_average_salary(
                employees
            )

            print(
                f"Average Salary : "
                f"{average_salary:.2f}"
            )

        case "11":

            employees: list[dict] = get_report(
                employee_file,
                salary_file
            )

            check_salary_condition(
                employees
            )

        case "12":

            print("Exiting...")
            break

        case _:

            print("Invalid choice.")