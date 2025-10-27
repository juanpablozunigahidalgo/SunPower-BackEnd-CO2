from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from app.core.database import get_db
from app.services.emissions import compute_company_emissions_kg
from app.services.solar import compensated_emissions_for_company
from app.schemas.emissions import GrossEmissionsOut, NetEmissionsOut

router = APIRouter(tags=["emissions"])

@router.get("/companies/{company_id}/emissions", response_model=GrossEmissionsOut)
def get_gross_emissions(
    company_id: int,
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db),
):
    res = compute_company_emissions_kg(db, company_id, date_from, date_to)
    return {
        "gross_emissions_kg": res["gross_emissions_kg"],
        "by_category": res["by_category"]
    }

@router.get("/companies/{company_id}/net-emissions", response_model=NetEmissionsOut)
def get_net_emissions(
    company_id: int,
    date_from: date,
    date_to: date,
    db: Session = Depends(get_db),
):
    gross = compute_company_emissions_kg(db, company_id, date_from, date_to)
    comp_kg = compensated_emissions_for_company(db, company_id, date_from, date_to)
    net_val = gross["gross_emissions_kg"] - comp_kg
    if net_val < 0:
        net_val = 0.0
    return {
        "gross_emissions_kg": gross["gross_emissions_kg"],
        "compensated_kg": comp_kg,
        "net_emissions_kg": net_val,
        "by_category": gross["by_category"]
    }
