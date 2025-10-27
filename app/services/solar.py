from sqlalchemy.orm import Session
from datetime import date
from app.models.solar import SolarProject, SolarAllocation

def _annual_kwh(project: SolarProject) -> float:
    return (
        project.capacity_kwp
        * project.performance_ratio
        * project.peak_sun_hours_per_day
        * 365.0
    )

def _annual_avoided_kg(project: SolarProject) -> float:
    return _annual_kwh(project) * project.grid_factor_kg_per_kwh

def _overlap_days(a_start: date, a_end: date, b_start: date, b_end: date) -> int:
    start = max(a_start, b_start)
    end = min(a_end, b_end)
    if end < start:
        return 0
    return (end - start).days + 1

def compensated_emissions_for_company(
    db: Session,
    company_id: int,
    period_start: date,
    period_end: date
) -> float:
    allocs = db.query(SolarAllocation).filter(
        SolarAllocation.company_id == company_id
    ).all()

    total_comp_kg = 0.0

    for alloc in allocs:
        project = db.query(SolarProject).get(alloc.project_id)
        if not project:
            continue

        days = _overlap_days(
            alloc.start_date, alloc.end_date,
            period_start, period_end
        )
        if days <= 0:
            continue

        yearly_kg = _annual_avoided_kg(project)
        fraction_of_year = days / 365.0
        alloc_kg = yearly_kg * alloc.allocation_fraction * fraction_of_year
        total_comp_kg += alloc_kg

    return float(f"{total_comp_kg:.6f}")
