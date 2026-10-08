from datetime import date
from pydantic import BaseModel, Field
class SalaryReport(BaseModel):
    employee_id: int = Field(gt=0)
    employee_name: str = Field(min_length=1)
    department: str = Field(min_length=1)
    designation: str = Field(min_length=1)
    experience: int = Field(ge=0)
    basic_salary: float = Field(gt=0)
    hra: float = Field(ge=0)
    da: float = Field(ge=0)
    bonus: float = Field(ge=0)
    net_salary: float = Field(ge=0)
    updated_date: date