import json
def display_employees( employee_file):
    try:
        with open(employee_file , "r") as file:
            employee_data = json.load(file)

        return employee_data

    except FileNotFoundError :
        print(f"File Not Found :{employee_file}")
        return []

    except json.JSONDecodeError:
        print(f"Invalid JSON Format :{employee_file}")
        return []
        


def get_high_salary_employee(employee_file,salary_file):
    try:
        with open(employee_file , "r") as emp_file:
            employee_data = json.load(emp_file)

        with open(salary_file , "r") as sal_file:
            salary_data = json.load(sal_file)

        high_salary_record = salary_data[0]

        for salary in salary_data:
            if salary["basic_salary"] > high_salary_record["basic_salary"]:
                high_salary_record = salary

        for employee in employee_data:
            if employee["employee_id"] == high_salary_record["employee_id"] :
                return {
                    "employee_id" :employee["employee_id"],
                    "employee_name":employee["employee_name"],
                    "department": employee["department"],
                    "designation": employee["designation"],
                    "experience" :employee["experience"],
                    "basic_salary": high_salary_record["basic_salary"],
                    "hra": high_salary_record["hra"],
                    "da": high_salary_record["da"],
                    "bonus": high_salary_record["bonus"],
                    "net_salary": high_salary_record["net_salary"]
                }           

        
    except FileNotFoundError :
        print(f"File Not Found")
        return []
    
    except json.JSONDecodeError:
        print(f"Invalid JSON Format")
        return []


    


