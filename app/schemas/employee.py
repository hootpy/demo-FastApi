from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: str
    email: str
    password: str
