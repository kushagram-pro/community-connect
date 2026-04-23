from fastapi import APIRouter
from app.services.gemini import classify_need
from app.db.firestore import db

router = APIRouter()

@router.post("/")
async def intake(data: dict):
    description = data.get("description", "")

    if not description:
        return {"error": "description is required"}

    ai_output = classify_need(description)

    doc = {
        "description": description,
        "ai_output": ai_output,
        "status": "open"
    }

    # Store in Firestore
    db.collection("needs").add(doc)

    return {
        "message": "Need stored successfully",
        "data": doc
    }