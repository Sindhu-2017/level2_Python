from datetime import date
from pydantic import BaseModel, Field
class Salary(BaseModel):
    employee_id: int = Field(gt=0)
    basic_salary: float = Field(gt=0)
    hra: float = Field(ge=0)
    da: float = Field(ge=0)
    bonus: float = Field(ge=0)
    net_salary: float = Field(ge=0)
    updated_date: date