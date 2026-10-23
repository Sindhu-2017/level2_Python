import json
from exceptions.custom_exceptions import DataFileError
class EmployeeRepository:

    def __init__(self, employee_file):
        self.employee_file = employee_file

    def get_all(self) -> list[dict]:
        try:
            with open(self.employee_file, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            raise DataFileError("Employee file not found.")

        except json.JSONDecodeError:
            raise DataFileError("Invalid employee JSON format.")