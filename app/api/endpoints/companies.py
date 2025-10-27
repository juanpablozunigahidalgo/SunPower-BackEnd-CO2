from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyOut

router = APIRouter(prefix="/companies", tags=["companies"])

@router.post("/", response_model=CompanyOut)
def create_company(payload: CompanyCreate, db: Session = Depends(get_db)):
    c = Company(
        name=payload.name,
        sector=payload.sector,
        country=payload.country
    )
    db.add(c)
    db.commit()
    db.refresh(c)
    return c
