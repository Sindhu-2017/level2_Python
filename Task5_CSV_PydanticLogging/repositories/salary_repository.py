import csv
import logging
from exceptions.custom_exceptions import DataFileError
from models.salary_model import Salary
from pydantic import ValidationError

logger = logging.getLogger(__name__)

class SalaryRepository:

    def __init__(self, salary_file):
        self.salary_file = salary_file

    async def get_all(self) -> list[dict]:
        logger.info(
            "Reading salary data from %s",self.salary_file
        )

        try:
            with open(self.salary_file, "r", newline="") as file:
                salaries = list(csv.DictReader(file))
                salaries = [Salary(**salary) for salary in salaries]

                logger.info(
                    "Salary records validated successfully"
                )

                return salaries

        except FileNotFoundError:

            logger.error(
                "Salary file not found: %s",self.salary_file
            )

            raise DataFileError(self.salary_file)
        except ValidationError as e:

                logger.error(
                    "Salary data validation failed: %s",e
                )
                
                print(e.errors())

    async def add(self, new_salary: dict) -> None:
        
        logger.info(
            "Adding salary record for employee %s",new_salary.employee_id
        )

        salary_data = await self.get_all()
        salary_data.append(new_salary)
        fieldnames = [
            "employee_id",
            "basic_salary",
            "hra",
            "da",
            "bonus",
            "net_salary",
            "updated_date"
        ]

        with open(self.salary_file,"w",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for salary in salary_data:
                writer.writerow(salary.model_dump())

        logger.info(
            "Salary record saved successfully for employee %s",new_salary.employee_id
        )


