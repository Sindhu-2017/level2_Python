class EmployeeAnalytics:
    def __init__(self,employees: list[dict]):

        self.employees = employees

    # displaying employees
    def display_employees(self) -> None:

        for number,employee in enumerate(self.employees,start=1):
            print(f"{number}. ID: {employee['employee_id']} - {employee['employee_name']} - {employee['department']} - Experience: {employee['experience']}")


    # get departments
    def get_departments(self) -> set[str]:
        return {employee["department"] for employee in self.employees}

    
    # sort by salary
    def sort_by_salary(self) -> list[dict]:
        return sorted(self.employees,key=lambda employee: employee["net_salary"],reverse=True)
    
    # sort by experience
    def sort_by_experience(self) -> list[dict]:
        return sorted(self.employees,key=lambda employee: employee["experience"],reverse=True)

    
    # highest salary employee
    def get_highest_salary_employee(self) -> dict | None:
        if not self.employees:
            return None

        return max(self.employees,key=lambda employee: employee["net_salary"])
    

    # search employees by dept
    def get_department_employees(self,department: str) -> list[dict]:
        return [employee for employee in self.employees if employee["department"].lower() == department.lower()]

    
    # get experienced employees
    def get_experienced_employees(self,minimum_experience: int) -> list[dict]:
        return [employee for employee in self.employees if employee["experience"] >= minimum_experience]
    
    # calculating average salary
    def calculate_average_salary(self) -> float:
        if not self.employees:
            return 0

        return sum(employee["net_salary"] for employee in self.employees) / len(self.employees)
    
    # checking salary condition
    def check_salary_condition(self) -> None:
        salaries = [employee["net_salary"] for employee in self.employees]

        print("All employees have salary above 30000:",all(salary > 30000 for salary in salaries))
        print("At least one employee has salary above 60000:",any(salary > 60000 for salary in salaries))