import json
from pathlib import Path


def get_employees(employee_file: Path) -> list[dict]:

    try:
        with open(employee_file, "r") as file:
            employee_data: list[dict] = json.load(file)

        return employee_data

    except FileNotFoundError:
        print("File Not Found")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON Format")
        return []