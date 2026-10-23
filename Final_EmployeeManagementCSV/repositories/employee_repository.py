import csv
import asyncio
from exceptions.custom_exceptions import DataFileError
from models.employee_model import Employee
from pydantic import ValidationError
import logging
logger = logging.getLogger(__name__)

class EmployeeRepository:

    def __init__(self, employee_file):
        self.employee_file = employee_file

    async def get_all(self) -> list[dict]:
        logger.info(
            "Reading employee data from %s",self.employee_file
        )

        try:
            with open(self.employee_file, "r", newline="") as file:
                employees = list(csv.DictReader(file))

                employees = [Employee(**employee) for employee in employees]
                logger.info(
                    "Employee records validated successfully"
                )
                return employees

        except FileNotFoundError:
            logger.error(
                "Employee file not found: %s",self.employee_file
            )
            raise DataFileError(self.employee_file)
        except ValidationError as e:
            logger.error(
                "Employee data validation failed: %s",e
            )
            print(e.errors())