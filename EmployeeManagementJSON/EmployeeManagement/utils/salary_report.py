import json
from pathlib import Path


def get_report(
    employee_file: Path,
    salary_file: Path
) -> list[dict]:

    try:
        with open(employee_file, "r") as file:
            employee_data: list[dict] = json.load(file)

        with open(salary_file, "r") as file:
            salary_data: list[dict] = json.load(file)

        salary_report: list[dict] = []

        for employee in employee_data:

            latest_salary: dict | None = None

            for salary in salary_data:

                if employee["employee_id"] == salary["employee_id"]:

                    if (
                        latest_salary is None
                        or salary["updated_date"]
                        > latest_salary["updated_date"]
                    ):
                        latest_salary = salary

            if latest_salary:

                report: dict = {
                    "employee_id": employee["employee_id"],
                    "employee_name": employee["employee_name"],
                    "department": employee["department"],
                    "designation": employee["designation"],
                    "experience": employee["experience"],
                    "basic_salary": latest_salary["basic_salary"],
                    "hra": latest_salary["hra"],
                    "da": latest_salary["da"],
                    "bonus": latest_salary["bonus"],
                    "net_salary": latest_salary["net_salary"],
                    "updated_date": latest_salary["updated_date"]
                }

                salary_report.append(report)

        return salary_report

    except FileNotFoundError:
        print("File Not Found")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON Format")
        return []