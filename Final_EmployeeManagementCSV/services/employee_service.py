from exceptions.custom_exceptions import EmployeeNotFoundError
import logging

logger = logging.getLogger(__name__)

class EmployeeService:

    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    async def get_employees(self) -> list[dict]:

        logger.info("Fetching employees")

        return await self.employee_repository.get_all()

    async def check_employee(self, employee_id: int) -> None:

        logger.info(
            "Checking employee ID: %s",employee_id
        )

        employees = await self.get_employees()

        if not any(employee.employee_id == employee_id for employee in employees):
            logger.warning(
                "Employee ID %s was not found",employee_id
            )
            raise EmployeeNotFoundError(employee_id)