class Employee:

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    # Responsibility 1: Calculate salary
    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        return self.basic_salary + hra + da

    # Responsibility 2: Save employee
    def save_employee(self):
        print(f"Employee {self.name} saved to database")

    # Responsibility 3: Generate salary slip
    def generate_salary_slip(self):
        salary = self.calculate_salary()
        print(f"Salary Slip")
        print(f"Employee: {self.name}")
        print(f"Salary: {salary}")

    # Responsibility 4: Send email
    def send_email(self):
        print(f"Salary slip sent to {self.name}")
        

employee = Employee("Ravi", 30000)

employee.calculate_salary()
employee.save_employee()
employee.generate_salary_slip()
employee.send_email()