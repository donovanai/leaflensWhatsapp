from fastapi import APIRouter, HTTPException, Depends
from src.config import WHATSAPP_API_KEY
from src.auth import get_current_user
from src.ai import analyze_plant_image
from src.database import increment_message_count, check_message_limit

router = APIRouter()

@router.post("/receive")
async def receive_message(image: str, user=Depends(get_current_user)):
    if check_message_limit(user["id"]):
        description = analyze_plant_image(image)
        increment_message_count(user["id"])
        return {"description": description}
    else:
        return {"message": "You have reached your free message limit. Please subscribe to continue."}