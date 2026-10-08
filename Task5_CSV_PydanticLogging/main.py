from config import EMPLOYEE_FILE, SALARY_FILE

from repositories.employee_repository import EmployeeRepository
from repositories.salary_repository import SalaryRepository
from services.employee_service import EmployeeService
from services.salary_service import SalaryService
from services.report_service import ReportService
from utilities.employee_operations import EmployeeOperations

from exceptions.custom_exceptions import (EmployeeNotFoundError,InvalidSalaryError,DataFileError)
import asyncio
import logging

logger = logging.getLogger(__name__)

employee_repository = EmployeeRepository(EMPLOYEE_FILE)
salary_repository = SalaryRepository(SALARY_FILE)

employee_service = EmployeeService(employee_repository)
salary_service = SalaryService(salary_repository)
report_service = ReportService(employee_repository,salary_repository)

async def main():
    logger.info("Employee Management System started")
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

        logger.info("User selected option: %s", choice)

        try:
            match choice:
                case "1":
                    logger.info("Displaying employees")
                    employees = await employee_service.get_employees()

                    if employees:
                        EmployeeOperations(employees).display_employees()
                    else:
                        # print("No employee records found...")
                        logger.warning("No employee records found")

                case "2":
                    logger.info("Adding new salary record")
                    employee_id = int(input("Enter employee ID: "))
                    await employee_service.check_employee(employee_id)

                    basic_salary = float(input("Enter basic salary: "))
                    salary = await salary_service.add_salary(employee_id,basic_salary)

                    logger.info(
                        "Salary added successfully for employee %s",employee_id
                    )

                    print(f"HRA : {salary.hra}")
                    print(f"DA : {salary.da}")
                    print(f"Bonus : {salary.bonus}")
                    print(f"Net Salary : {salary.net_salary}")

                case "3":
                    logger.info("Finding highest salary employee")
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    employee = emp_operations.get_highest_salary_employee()

                    if employee:
                        print(f"Name : {employee.employee_name}")
                        print(f"Department : {employee.department}")
                        print(f"Salary : {employee.net_salary}")
                    else:
                        logger.warning("No salary records found")
                        print("No salary records found.")

                case "4":
                    logger.info("Generating salary report")
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
                        logger.warning("No salary records available")
                        print("No salary records found.")

                case "5":
                    logger.info("Displaying departments")
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    for department in emp_operations.get_departments():
                        print(department)

                case "6":
                    logger.info("Sorting employees by experience")
                    employees =await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    sorted_employees = emp_operations.sort_by_salary()
                    EmployeeOperations(sorted_employees).display_employees()

                case "7":
                    logger.info("Sorting employees by experience")
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    sorted_employees = emp_operations.sort_by_experience()
                    EmployeeOperations(sorted_employees).display_employees()

                case "8":
                    department = input("Enter department: ")
                    logger.info(
                        "Searching employees in department: %s",department
                    )
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    result = emp_operations.get_department_employees(department)

                    if result:
                        EmployeeOperations(result).display_employees()
                    else:
                        logger.warning(
                            "No employees found in department: %s", department
                        )
                        print("No employees found.")

                case "9":
                    experience = int(input("Enter experience  :"))
                    logger.info(
                        "Searching employees with experience >= %s",experience
                    )
                    employees =await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    result = emp_operations.get_experienced_employees(experience)
                    if result:
                        EmployeeOperations(result).display_employees()
                    else:
                        logger.warning("No employees found with required experience")
                        print("No employees found.")


                case "10":
                    logger.info("Checking salary conditions")
                    employees = await report_service.get_report()
                    emp_operations = EmployeeOperations(employees)
                    emp_operations.check_salary_condition()

                case "11":

                    logger.info("Downloading salary report")
                    reports = await report_service.get_report()

                    if reports:
                        report_service.save_report(reports)
                        logger.info("Salary report saved successfully")
                        print("Salary report saved successfully.")
                    else:
                        logger.warning("Cannot save report because no salary records exist")
                        print("No salary records found.")

                case "12":
                    logger.info("Employee Management System stopped")
                    print("Exiting...")
                    break

                case _:

                    logger.warning("Invalid menu choice: %s", choice)
                    print("Invalid choice.")

        except ValueError:
            logger.error("Invalid numeric input entered by user")
            print("Enter valid numbers.")

        except EmployeeNotFoundError as error:
            logger.warning("Employee not found: %s",error.employee_id)
            print(error)

        except InvalidSalaryError as error:
            logger.warning("Invalid salary entered: %s",error.salary)
            print(error)

        except DataFileError as error:
            logger.error("Data file error: %s", error.file_name )
            print(error)

        finally:
            print("Program executed successfully...")

asyncio.run(main())