from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.endpoints import companies, activities, solar, emissions, health

# Crear tablas al iniciar (solo dev con SQLite)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SunPowerScope API",
    description="Track company CO₂ emissions and solar compensation.",
    version="0.1.0",
)

# Routers
app.include_router(health.router)
app.include_router(companies.router)
app.include_router(activities.router)
app.include_router(solar.router)
app.include_router(emissions.router)
