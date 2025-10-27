from pydantic import BaseModel
from typing import Dict

class GrossEmissionsOut(BaseModel):
    gross_emissions_kg: float
    by_category: Dict[str, float]

class NetEmissionsOut(BaseModel):
    gross_emissions_kg: float
    compensated_kg: float
    net_emissions_kg: float
    by_category: Dict[str, float]
