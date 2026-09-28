import json
from pathlib import Path


def display_employees(employee_file: Path) -> list[dict]:
    try:
        with open(employee_file, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File Not Found")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON Format")
        return []