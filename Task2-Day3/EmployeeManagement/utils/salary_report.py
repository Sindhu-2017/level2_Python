import json
def display_salary_report(employee_file , salary_file):
    try:
        with open(employee_file,"r") as emp_file:
            employee_data = json.load(emp_file)

        with open(salary_file,"r") as sal_file:
            salary_data = json.load(sal_file)

        salary_report =[]

        for employee in employee_data:
            for salary in salary_data:
                if employee["employee_id"] == salary["employee_id"]:
                    report ={
                        "employee_id" :employee["employee_id"],
                        "employee_name":employee["employee_name"],
                        "department": employee["department"],
                        "designation": employee["designation"],
                        "experience" :employee["experience"],
                        "basic_salary": salary["basic_salary"],
                        "hra": salary["hra"],
                        "da": salary["da"],
                        "bonus": salary["bonus"],
                        "net_salary": salary["net_salary"]
                    }

                    salary_report.append(report)



        return salary_report
        
    
    except FileNotFoundError :
        print(f"File Not Found ")
        return []
    
    except json.JSONDecodeError:
        print(f"Invalid JSON Format")
        return []