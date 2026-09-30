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