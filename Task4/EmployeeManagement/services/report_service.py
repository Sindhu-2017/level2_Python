from config import REPORT_FILE
class ReportService:

    def __init__(self, employee_repository, salary_repository):
        self.employee_repository = employee_repository
        self.salary_repository = salary_repository

    def get_report(self) -> list[dict]:
        employees = self.employee_repository.get_all()
        salaries = self.salary_repository.get_all()

        reports = []

        for employee in employees:
            latest_salary = None

            for salary in salaries:
                if employee["employee_id"] == salary["employee_id"]:
                    if (latest_salary is None or salary["updated_date"] > latest_salary["updated_date"]):
                        latest_salary = salary

            if latest_salary:
                report = {
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
                reports.append(report)
        return reports


    def save_report(self, reports):

        with open(REPORT_FILE, "w") as file:

            for number, report in enumerate(reports, start=1):

                file.write(
                    f"\n{number}. ID : {report['employee_id']} - "
                    f"{report['employee_name']} - "
                    f"{report['department']}\n"
                )

                file.write(f"Designation : {report['designation']}\n")
                file.write(f"Experience : {report['experience']}\n")
                file.write(f"Basic Salary : {report['basic_salary']}\n")
                file.write(f"HRA : {report['hra']}\n")
                file.write(f"DA : {report['da']}\n")
                file.write(f"Bonus : {report['bonus']}\n")
                file.write(f"Net Salary : {report['net_salary']}\n")
                file.write(f"Updated Date : {report['updated_date']}\n")
                file.write("_" * 40 + "\n")