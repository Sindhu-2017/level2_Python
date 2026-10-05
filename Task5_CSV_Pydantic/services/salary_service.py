from datetime import date
from exceptions.custom_exceptions import InvalidSalaryError
from config import (HRA_PERCENTAGE,DA_PERCENTAGE,BONUS_PERCENTAGE)
from models.salary_model import Salary
class SalaryService:

    def __init__(self, salary_repository):
        self.salary_repository = salary_repository

    def calculate_hra(self, basic_salary: float) -> float:
        return basic_salary * HRA_PERCENTAGE

    def calculate_da(self, basic_salary: float) -> float:
        return basic_salary * DA_PERCENTAGE

    def calculate_bonus(self, basic_salary: float) -> float:
        return basic_salary * BONUS_PERCENTAGE

    def calculate_net_salary(self,basic_salary: float,hra: float,da: float,bonus: float) -> float:
        return basic_salary + hra + da + bonus

    def add_salary(self, employee_id: int, basic_salary: float) -> dict:
        if basic_salary <= 0:
            raise InvalidSalaryError("Salary must be greater than zero.")

        hra = self.calculate_hra(basic_salary)
        da = self.calculate_da(basic_salary)
        bonus = self.calculate_bonus(basic_salary)

        net_salary = self.calculate_net_salary(basic_salary,hra,da,bonus)
        # salary_data = {
        #     "employee_id": employee_id,
        #     "basic_salary": basic_salary,
        #     "hra": hra,
        #     "da": da,
        #     "bonus": bonus,
        #     "net_salary": net_salary,
        #     "updated_date": date.today().isoformat()
        # }

        salary_data = Salary(
            employee_id=employee_id,
            basic_salary=basic_salary,
            hra=hra,
            da=da,
            bonus=bonus,
            net_salary=net_salary,
            updated_date=date.today()
        )

        self.salary_repository.add(salary_data)
        return salary_data