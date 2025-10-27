from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), index=True)
    category = Column(String)   # e.g. "electricity"
    amount = Column(Float)      # e.g. 1200
    unit = Column(String)       # e.g. "kWh"
    date = Column(Date)

    company = relationship("Company")
