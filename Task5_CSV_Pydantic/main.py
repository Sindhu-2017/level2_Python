from config import EMPLOYEE_FILE, SALARY_FILE

from repositories.employee_repository import EmployeeRepository
from repositories.salary_repository import SalaryRepository
from services.employee_service import EmployeeService
from services.salary_service import SalaryService
from services.report_service import ReportService
from utilities.employee_operations import EmployeeOperations

from exceptions.custom_exceptions import (EmployeeNotFoundError,InvalidSalaryError,DataFileError)
import asyncio

employee_repository = EmployeeRepository(EMPLOYEE_FILE)
salary_repository = SalaryRepository(SALARY_FILE)

employee_service = EmployeeService(employee_repository)
salary_service = SalaryService(salary_repository)
report_service = ReportService(employee_repository,salary_repository)

async def main():
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
        print("9.Display experienced employees")
        print("10.Check Salary Condition")
        print("11.Download Salary Report")
        print("12.Exit")

        choice = input("Enter your choice: ")

        try:
            match choice:
                case "1":
                    employees = await employee_service.get_employees()

                    if employees:
                        EmployeeOperations(employees).display_employees()
                    else:
                        print("No employee records found...")

                case "2":
                    employee_id = int(input("Enter employee ID: "))
                    await employee_service.check_employee(employee_id)

                    basic_salary = float(input("Enter basic salary: "))
                    salary = salary_service.add_salary(employee_id,basic_salary)
                    print(f"HRA : {salary.hra}")
                    print(f"DA : {salary.da}")
                    print(f"Bonus : {salary.bonus}")
                    print(f"Net Salary : {salary.net_salary}")

                case "3":
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    employee = emp_operations.get_highest_salary_employee()

                    if employee:
                        print(f"Name : {employee.employee_name}")
                        print(f"Department : {employee.department}")
                        print(f"Salary : {employee.net_salary}")
                    else:
                        print("No salary records found.")

                case "4":
                    reports = await report_service.get_report()
                    if reports:
                        for number, report in enumerate(reports, start=1):
                            print(
                                f"\n{number}. "
                                f"ID : {report.employee_id} - "
                                f"{report.employee_name} - "
                                f"{report.department}"
                            )

                            print(f"Designation : {report.designation}")
                            print(f"Experience : {report.experience}")
                            print(f"Basic Salary : {report.basic_salary}")
                            print(f"HRA : {report.hra}")
                            print(f"DA : {report.da}")
                            print(f"Bonus : {report.bonus}")
                            print(f"Net Salary : {report.net_salary}")
                            print(f"Updated Date : {report.updated_date}")
                            print("_" * 40)

                    else:
                        print("No salary records found.")

                case "5":
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    for department in emp_operations.get_departments():
                        print(department)

                case "6":
                    employees =await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    sorted_employees = emp_operations.sort_by_salary()
                    EmployeeOperations(sorted_employees).display_employees()

                case "7":
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    sorted_employees = emp_operations.sort_by_experience()
                    EmployeeOperations(sorted_employees).display_employees()

                case "8":
                    department = input("Enter department: ")
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    result = emp_operations.get_department_employees(department)

                    if result:
                        EmployeeOperations(result).display_employees()
                    else:
                        print("No employees found.")

                case "9":
                    experience = int(input("Enter experience  :"))
                    employees =await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    result = emp_operations.get_experienced_employees(experience)
                    if result:
                        EmployeeOperations(result).display_employees()
                    else:
                        print("No employees found.")

                case "10":

                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    emp_operations.check_salary_condition()

                case "11":

                    reports = await report_service.get_report()

                    if reports:
                        report_service.save_report(reports)
                        print("Salary report saved successfully.")
                    else:
                        print("No salary records found.")

                case "12":
                    print("Exiting...")
                    break

                case _:

                    print("Invalid choice.")

        except ValueError:
            print("Enter valid numbers.")

        except EmployeeNotFoundError as error:
            print(error)

        except InvalidSalaryError as error:
            print(error)

        except DataFileError as error:
            print(error)

        finally:
            print("Program executed successfully...")

asyncio.run(main())