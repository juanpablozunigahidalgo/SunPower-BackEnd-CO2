from pydantic import BaseModel
from datetime import date

class SolarProjectCreate(BaseModel):
    name: str
    location_country: str
    capacity_kwp: float
    performance_ratio: float
    peak_sun_hours_per_day: float
    grid_factor_kg_per_kwh: float
    commissioning_date: date

class SolarProjectOut(BaseModel):
    id: int
    name: str
    location_country: str
    capacity_kwp: float
    performance_ratio: float
    peak_sun_hours_per_day: float
    grid_factor_kg_per_kwh: float
    commissioning_date: date

    class Config:
        from_attributes = True

class SolarAllocationCreate(BaseModel):
    company_id: int
    project_id: int
    allocation_fraction: float
    start_date: date
    end_date: date

class SolarAllocationOut(BaseModel):
    id: int
    company_id: int
    project_id: int
    allocation_fraction: float
    start_date: date
    end_date: date

    class Config:
        from_attributes = True
