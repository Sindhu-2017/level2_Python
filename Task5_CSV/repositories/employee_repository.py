import csv
import asyncio
from exceptions.custom_exceptions import DataFileError

class EmployeeRepository:

    def __init__(self, employee_file):
        self.employee_file = employee_file

    async def get_all(self) -> list[dict]:

        try:
            with open(self.employee_file, "r", newline="") as file:
                employees = list(csv.DictReader(file))

                for employee in employees:
                    employee["employee_id"] = int(employee["employee_id"])
                    employee["experience"] = int(employee["experience"])

                return employees

        except FileNotFoundError:
            raise DataFileError("Employee file not found.")