import json
from pathlib import Path


def calculate_hra(basic_salary: float) -> float:
    return basic_salary * 0.20


def calculate_da(basic_salary: float) -> float:
    return basic_salary * 0.10


def calculate_bonus(basic_salary: float) -> float:
    return basic_salary * 0.05


def calculate_net_salary(
    basic_salary: float,
    hra: float,
    da: float,
    bonus: float
) -> float:

    return basic_salary + hra + da + bonus


def add_salary(
    salary_file: Path,
    new_data: dict
) -> None:

    try:
        with open(salary_file, "r") as file:
            salary_data: list[dict] = json.load(file)

        salary_data.append(new_data)

        with open(salary_file, "w") as file:
            json.dump(salary_data, file, indent=4)

        print("Salary record added successfully.")

    except FileNotFoundError:
        print("File Not Found")

    except json.JSONDecodeError:
        print("Invalid JSON Format")