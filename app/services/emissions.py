from sqlalchemy.orm import Session
from datetime import date
from app.models.activity import Activity
from app.models.emission_factor import EmissionFactor

def compute_company_emissions_kg(
    db: Session,
    company_id: int,
    date_from: date | None,
    date_to: date | None
):
    q = db.query(Activity).filter(Activity.company_id == company_id)
    if date_from:
        q = q.filter(Activity.date >= date_from)
    if date_to:
        q = q.filter(Activity.date <= date_to)

    totals_by_category: dict[str, float] = {}
    gross_total = 0.0

    for act in q.all():
        ef = db.query(EmissionFactor).filter_by(
            category=act.category,
            unit=act.unit
        ).first()
        if not ef:
            continue
        kg = act.amount * ef.factor_kg_per_unit
        totals_by_category[act.category] = totals_by_category.get(act.category, 0.0) + kg
        gross_total += kg

    return {
        "gross_emissions_kg": gross_total,
        "by_category": totals_by_category
    }
