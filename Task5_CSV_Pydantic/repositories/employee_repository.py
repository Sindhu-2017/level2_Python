import csv
import asyncio
from exceptions.custom_exceptions import DataFileError
from models.employee_model import Employee
from pydantic import ValidationError
class EmployeeRepository:

    def __init__(self, employee_file):
        self.employee_file = employee_file

    async def get_all(self) -> list[dict]:

        try:
            with open(self.employee_file, "r", newline="") as file:
                employees = list(csv.DictReader(file))

                employees = [Employee(**employee) for employee in employees]
                return employees

        except FileNotFoundError:
            raise DataFileError(self.employee_file)
        except ValidationError as e:
            print(e.errors())