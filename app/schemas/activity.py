from pydantic import BaseModel
from datetime import date

class ActivityCreate(BaseModel):
    company_id: int
    category: str
    amount: float
    unit: str
    date: date

class ActivityOut(BaseModel):
    id: int
    company_id: int
    category: str
    amount: float
    unit: str
    date: date

    class Config:
        from_attributes = True
