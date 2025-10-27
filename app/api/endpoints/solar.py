from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.solar import SolarProject, SolarAllocation
from app.schemas.solar import (
    SolarProjectCreate, SolarProjectOut,
    SolarAllocationCreate, SolarAllocationOut
)

router = APIRouter(prefix="/solar", tags=["solar"])

@router.post("/projects/", response_model=SolarProjectOut)
def create_solar_project(payload: SolarProjectCreate, db: Session = Depends(get_db)):
    p = SolarProject(
        name=payload.name,
        location_country=payload.location_country,
        capacity_kwp=payload.capacity_kwp,
        performance_ratio=payload.performance_ratio,
        peak_sun_hours_per_day=payload.peak_sun_hours_per_day,
        grid_factor_kg_per_kwh=payload.grid_factor_kg_per_kwh,
        commissioning_date=payload.commissioning_date
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

@router.post("/allocations/", response_model=SolarAllocationOut)
def create_solar_allocation(payload: SolarAllocationCreate, db: Session = Depends(get_db)):
    alloc = SolarAllocation(
        company_id=payload.company_id,
        project_id=payload.project_id,
        allocation_fraction=payload.allocation_fraction,
        start_date=payload.start_date,
        end_date=payload.end_date
    )
    db.add(alloc)
    db.commit()
    db.refresh(alloc)
    return alloc
