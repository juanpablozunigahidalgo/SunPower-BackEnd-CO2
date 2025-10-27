from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    sector: str | None = None
    country: str | None = None

class CompanyOut(BaseModel):
    id: int
    name: str
    sector: str | None
    country: str | None

    class Config:
        from_attributes = True
