from fastapi import FastAPI
from app.routes import health, intake

app = FastAPI(title="CommunityConnect API")

app.include_router(health.router)
app.include_router(intake.router, prefix="/intake")