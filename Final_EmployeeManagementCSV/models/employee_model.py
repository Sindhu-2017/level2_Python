from pydantic import BaseModel, Field

class Employee(BaseModel):
    employee_id: int = Field(gt=0)
    employee_name: str = Field(min_length=1)
    department: str = Field(min_length=1)
    designation: str = Field(min_length=1)
    experience: int = Field(ge=0)