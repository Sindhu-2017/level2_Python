import json
from pathlib import Path


def display_salary_report(
    employee_file: Path,
    salary_file: Path
) -> list[dict]:

    try:
        with open(employee_file, "r") as file:
            employee_data = json.load(file)

        with open(salary_file, "r") as file:
            salary_data = json.load(file)

        salary_lookup = {
            salary["employee_id"]: salary
            for salary in salary_data
        }

        salary_report = []

        for employee in employee_data:

            salary = salary_lookup.get(
                employee["employee_id"]
            )

            if salary:

                report = {
                    "employee_id": employee["employee_id"],
                    "employee_name": employee["employee_name"],
                    "department": employee["department"],
                    "designation": employee["designation"],
                    "experience": employee["experience"],
                    "basic_salary": salary["basic_salary"],
                    "hra": salary["hra"],
                    "da": salary["da"],
                    "bonus": salary["bonus"],
                    "net_salary": salary["net_salary"],
                    "updated_date": salary["updated_date"]
                }

                salary_report.append(report)

        return salary_report

    except FileNotFoundError:
        print("File Not Found")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON Format")
        return []