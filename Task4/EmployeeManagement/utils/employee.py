import json
class EmployeeManager:
    def __init__(self,employee_file):
        self.employee_file = employee_file

    def get_employees(self) -> list[dict]:

        try:
            with open(self.employee_file,"r") as file:
                employee_data=json.load(file)
            return employee_data

        except FileNotFoundError:
            print("File Not Found")
            return []

        except json.JSONDecodeError:
            print("Invalid JSON Format")
            return []