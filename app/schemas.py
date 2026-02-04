from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    full_name: str
    job_title: str
    country: str
    salary: float


class EmployeeUpdate(BaseModel):
    salary: float | None = None


class EmployeeOut(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True
