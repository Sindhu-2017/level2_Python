import csv
import asyncio
from exceptions.custom_exceptions import DataFileError
from models.salary_model import Salary
class SalaryRepository:

    def __init__(self, salary_file):
        self.salary_file = salary_file

    async def get_all(self) -> list[dict]:
        try:
            with open(self.salary_file, "r", newline="") as file:
                salaries = list(csv.DictReader(file))

                # for salary in salaries:
                #     salary["employee_id"] = int(salary["employee_id"])
                #     salary["basic_salary"] = float(salary["basic_salary"])
                #     salary["hra"] = float(salary["hra"])
                #     salary["da"] = float(salary["da"])
                #     salary["bonus"] = float(salary["bonus"])
                #     salary["net_salary"] = float(salary["net_salary"])
                salaries = [Salary(**salary) for salary in salaries]
                return salaries

        except FileNotFoundError:
            raise DataFileError("Salary file not found.")

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
            # writer.writerows(salary_data)
            for salary in salary_data:
                writer.writerow(salary.model_dump(mode="json"))


