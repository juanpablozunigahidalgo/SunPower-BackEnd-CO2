from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class SolarProject(Base):
    __tablename__ = "solar_projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    location_country = Column(String)
    capacity_kwp = Column(Float)
    performance_ratio = Column(Float)
    peak_sun_hours_per_day = Column(Float)
    grid_factor_kg_per_kwh = Column(Float)
    commissioning_date = Column(Date)

class SolarAllocation(Base):
    __tablename__ = "solar_allocations"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), index=True)
    project_id = Column(Integer, ForeignKey("solar_projects.id"), index=True)
    allocation_fraction = Column(Float) # 0..1
    start_date = Column(Date)
    end_date = Column(Date)

    company = relationship("Company")
    project = relationship("SolarProject")
