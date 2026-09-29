class Employee:

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary


class SalaryCalculator:

    def calculate_salary(self, employee):
        hra = employee.basic_salary * 0.20
        da = employee.basic_salary * 0.10

        return employee.basic_salary + hra + da


class EmployeeRepository:

    def save(self, employee):
        print(f"Employee {employee.name} saved to database")


class SalarySlipGenerator:

    def generate(self, employee, salary):
        print("\n----- SALARY SLIP -----")
        print(f"Employee : {employee.name}")
        print(f"Basic    : {employee.basic_salary}")
        print(f"Total    : {salary}")
        print("-----------------------")


class EmailService:

    def send(self, employee):
        print(f"Salary slip sent to {employee.name}")


employee = Employee("Ravi", 30000)

calculator = SalaryCalculator()
salary = calculator.calculate_salary(employee)

repository = EmployeeRepository()
repository.save(employee)

slip = SalarySlipGenerator()
slip.generate(employee, salary)

email = EmailService()
email.send(employee)