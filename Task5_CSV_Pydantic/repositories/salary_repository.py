import csv
import asyncio
from exceptions.custom_exceptions import DataFileError
from models.salary_model import Salary
from pydantic import ValidationError
class SalaryRepository:

    def __init__(self, salary_file):
        self.salary_file = salary_file

    async def get_all(self) -> list[dict]:
        try:
            with open(self.salary_file, "r", newline="") as file:
                salaries = list(csv.DictReader(file))
                salaries = [Salary(**salary) for salary in salaries]
                return salaries

        except FileNotFoundError:
            raise DataFileError(self.salary_file)
        except ValidationError as e:
                print(e.errors())

    async def add(self, new_salary: dict) -> None:
        salary_data = await self.get_all()
        salary_data.append(new_salary)
        fieldnames = [
            "employee_id",
            "basic_salary",
            "hra",
            "da",
            "bonus",
            "net_salary",
            "updated_date"
        ]

        with open(self.salary_file,"w",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for salary in salary_data:
                writer.writerow(salary.model_dump())
            


