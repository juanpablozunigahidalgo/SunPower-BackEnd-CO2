from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class EmissionFactor(Base):
    __tablename__ = "emission_factors"

    id = Column(Integer, primary_key=True)
    category = Column(String, index=True)
    unit = Column(String)
    factor_kg_per_unit = Column(Float)  # kg CO2e por unidad
