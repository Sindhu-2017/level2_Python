from dotenv import load_dotenv
import os
from utils.employee import EmployeeManager
from utils.salary import SalaryManager
from utils.salary_report import SalaryReport
from utils.analytics import EmployeeAnalytics
from pathlib import Path
from datetime import date

load_dotenv()

employee_file = Path(os.getenv("EMPLOYEE_FILE"))
salary_file = Path(os.getenv("SALARY_FILE"))


employee_manager = EmployeeManager(employee_file)
salary_manager = SalaryManager(salary_file)
salary_report = SalaryReport(employee_file,salary_file)


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
    print("12.Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            employees = employee_manager.get_employees()
            if employees:
                analytics = EmployeeAnalytics(employees)
                analytics.display_employees()
            else:
                print("No employee records found.")

        case "2":
            try:
                employee_id = int(input("Enter employee ID: "))
                basic_salary = float(input("Enter basic salary: "))

                hra = salary_manager.calculate_hra(basic_salary)
                da = salary_manager.calculate_da(basic_salary)
                bonus = salary_manager.calculate_bonus(basic_salary)
                net_salary = salary_manager.calculate_netsalary(basic_salary,hra,da,bonus)

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

                salary_manager.add_salary(new_salary_data)
                print(f"HRA : {hra}")
                print(f"DA : {da}")
                print(f"Bonus : {bonus}")
                print(f"Net Salary : {net_salary}")

            except ValueError:
                print("Enter valid numbers.")


        case "3":
            employees = salary_report.get_report()
            analytics = EmployeeAnalytics(employees)
            employee = analytics.get_highest_salary_employee()

            if employee:
                print(f"Name : {employee['employee_name']}")
                print(f"Department : {employee['department']}")
                print(f"Salary : {employee['net_salary']}")
            else:
                print("No salary records found.")


        case "4":
            reports = salary_report.get_report()
            if reports:
                for number,report in enumerate(reports,start=1):
                    print(f"\n{number}. ID : {report['employee_id']} - {report['employee_name']} - {report['department']}")
                    print(f"Designation : {report['designation']}")
                    print(f"Experience : {report['experience']}")
                    print(f"Basic Salary : {report['basic_salary']}")
                    print(f"HRA : {report['hra']}")
                    print(f"DA : {report['da']}")
                    print(f"Bonus : {report['bonus']}")
                    print(f"Net Salary : {report['net_salary']}")
                    print(f"Updated Date : {report['updated_date']}")
                    print("_" * 40)
            else:
                print("No salary records found")

        case "5":
            employees = salary_report.get_report()
            analytics = EmployeeAnalytics(employees)
            departments = analytics.get_departments()

            for department in departments:
                print(department)

        case "6":
            employees = salary_report.get_report()
            analytics = EmployeeAnalytics(employees)
            sorted_employees = analytics.sort_by_salary()
            EmployeeAnalytics(sorted_employees).display_employees()

        case "7":
            employees = salary_report.get_report()
            analytics = EmployeeAnalytics(employees)
            sorted_employees = analytics.sort_by_experience()
            EmployeeAnalytics(sorted_employees).display_employees()


        case "8":
            department = input("Enter department: ")
            employees = salary_report.get_report()
            analytics = EmployeeAnalytics(employees)

            result = analytics.get_department_employees(department)
            if result:
                EmployeeAnalytics(result).display_employees()
            else:
                print("No employees found.")

        case "9":
            try:
                minimum_experience = int(input("Enter minimum experience: "))
                employees = salary_report.get_report()
                analytics = EmployeeAnalytics(employees)
                result = analytics.get_experienced_employees(minimum_experience)

                if result:
                    EmployeeAnalytics(result).display_employees()
                else:
                    print("No employees found.")

            except ValueError:
                print("Enter valid experience.")


        case "10":
            employees = salary_report.get_report()
            analytics = EmployeeAnalytics(employees)
            average_salary = analytics.calculate_average_salary()
            print(f"Average Salary : {average_salary:.2f}")


        case "11":
            employees = salary_report.get_report()
            analytics = EmployeeAnalytics(employees)
            analytics.check_salary_condition()


        case "12":
            print("Exiting...")
            break


        case _:

            print("Invalid choice.")