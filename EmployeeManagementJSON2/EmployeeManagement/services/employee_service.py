from exceptions.custom_exceptions import EmployeeNotFoundError
class EmployeeService:

    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def get_employees(self) -> list[dict]:
        return self.employee_repository.get_all()

    def check_employee(self, employee_id: int) -> None:
        employees = self.get_employees()

        if not any(employee["employee_id"] == employee_id for employee in employees):
            raise EmployeeNotFoundError("Employee ID does not exist")