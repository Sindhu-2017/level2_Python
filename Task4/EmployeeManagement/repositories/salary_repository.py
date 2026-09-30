import json
from exceptions.custom_exceptions import DataFileError
class SalaryRepository:

    def __init__(self, salary_file):
        self.salary_file = salary_file

    def get_all(self) -> list[dict]:

        try:
            with open(self.salary_file, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            raise DataFileError("Salary file not found.")

        except json.JSONDecodeError:
            raise DataFileError("Invalid salary JSON format.")

    def add(self, new_salary: dict) -> None:

        salary_data = self.get_all()
        salary_data.append(new_salary)

        with open(self.salary_file, "w") as file:
            json.dump(salary_data, file, indent=4)