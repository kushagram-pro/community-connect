from fastapi import FastAPI
from app.routes import health, intake, volunteer, match

app = FastAPI(title="CommunityConnect API")

app.include_router(health.router)
app.include_router(intake.router, prefix="/intake")
app.include_router(match.router, prefix="/match")
app.include_router(volunteer.router, prefix="/volunteer")