import json

def update_salary(salary_file,employee_id,updated_salary):
    try:
        with open(salary_file , "r") as sal_file:
            salary_data = json.load(sal_file)

        for salary in salary_data:
            if salary["employee_id"] == employee_id:
                salary["basic_salary"] = updated_salary

        with open(salary_file,"w") as sal_file2:
            json.dump(salary_data,sal_file2,indent=4)

    except FileNotFoundError :
        print(f"File Not Found :{salary_file}")
                
    except json.JSONDecodeError:
       print(f"Invalid JSON Format :{salary_file}")


    else:
        print("Salary updated successfully..")

    

    
    