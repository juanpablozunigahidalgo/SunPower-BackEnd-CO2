from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.api.endpoints import companies, activities, solar, emissions, health

# Create tables on startup (SQLite dev mode)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SunPowerScope API",
    description="Track company CO₂ emissions and solar compensation.",
    version="0.1.0",
)

# 👇👇 CRITICAL: allow frontend on :5173 to call backend on :8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(companies.router)
app.include_router(activities.router)
app.include_router(solar.router)
app.include_router(emissions.router)
