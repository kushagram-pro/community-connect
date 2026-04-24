from fastapi import APIRouter
from app.db.firestore import db

router = APIRouter()

@router.post("/")
async def register_volunteer(data: dict):
    required_fields = ["name", "skills", "location", "available", "max_distance"]

    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}
        
    db.collection("volunteers").add(data)

    return {"message": "Volunteer registered successfully", "data": data}