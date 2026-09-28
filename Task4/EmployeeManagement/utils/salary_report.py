import json
class SalaryReport:
    def __init__(self,employee_file,salary_file):
        self.employee_file = employee_file
        self.salary_file = salary_file

    def get_report(self) -> list[dict]:
        try:
            with open(self.employee_file,"r") as file:
                employee_data = json.load(file)

            with open(self.salary_file,"r") as file:
                salary_data = json.load(file)

            salary_report = []

            for employee in employee_data:
                for salary in salary_data:
                    if employee["employee_id"] == salary["employee_id"]:

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
                        break
                    
            return salary_report

        except FileNotFoundError:
            print("File Not Found")
            return []

        except json.JSONDecodeError:
            print("Invalid JSON Format")
            return []