from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate, ActivityOut

router = APIRouter(prefix="/activities", tags=["activities"])

@router.post("/", response_model=ActivityOut)
def create_activity(payload: ActivityCreate, db: Session = Depends(get_db)):
    a = Activity(
        company_id=payload.company_id,
        category=payload.category,
        amount=payload.amount,
        unit=payload.unit,
        date=payload.date
    )
    db.add(a)
    db.commit()
    db.refresh(a)
    return a
