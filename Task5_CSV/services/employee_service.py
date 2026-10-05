from exceptions.custom_exceptions import EmployeeNotFoundError
import asyncio
class EmployeeService:

    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    async def get_employees(self) -> list[dict]:
        return await self.employee_repository.get_all()

    async def check_employee(self, employee_id: int) -> None:
        employees = await self.get_employees()

        if not any(employee["employee_id"] == employee_id for employee in employees):
            raise EmployeeNotFoundError("Employee ID does not exist")