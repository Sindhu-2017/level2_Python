import json
class SalaryManager:

    def __init__(self,salary_file):
        self.salary_file = salary_file

    def calculate_hra(self,basic_salary: float) -> float:
        return basic_salary * 0.20

    def calculate_da(self,basic_salary: float) -> float:
        return basic_salary * 0.10

    def calculate_bonus(self,basic_salary: float) -> float:

         return basic_salary * 0.05


    def calculate_netsalary(self,basic_salary: float,hra:float,da:float,bonus:float) -> float:

        return basic_salary + hra + da + bonus
    

    def add_salary(self,new_data: dict) -> None:

        try:
            with open(self.salary_file,"r") as file:
                salary_data = json.load(file)

            salary_data.append(new_data)

            with open(self.salary_file,"w") as file:
                json.dump(salary_data,file,indent=4)

            print("Salary record added successfully.")

        except FileNotFoundError:
            print("File Not Found")

        except json.JSONDecodeError:
            print("Invalid JSON Format")