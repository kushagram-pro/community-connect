from fastapi import APIRouter
from app.db.firestore import db
from app.services.matcher import match_volunteers

router = APIRouter()

@router.post("/")
async def match(data: dict):
    need_id = data.get("need_id")

    if not need_id:
        return {"error": "need_id is required"}
    
    # Fetch need
    need_doc = db.collection("needs").document(need_id).get()
    if not need_doc.exists:
        return {"error": "Need not found"}
    
    need = need_doc.to_dict()
    category = need["ai_output"]["category"]

    # Fetch volunteers
    volunteers_ref = db.collection("volunteers").stream()
    
    volunteers = []
    for v in volunteers_ref:
        vol = v.to_dict()
        vol["id"] = v.id
        volunteers.append(vol)

    # Add simplified category for matching
    need_data = {
        "category": category
    }

    matches = match_volunteers(need_data, volunteers)

    return {"matches": matches}
