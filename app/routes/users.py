from fastapi import APIRouter
from app.crud import get_user_chats
from app.database import db
from bson import ObjectId


def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

router = APIRouter()

@router.get("/users/{user_id}/chats")
async def user_chats(user_id: str, page: int = 1, limit: int = 10):
    chats = await get_user_chats(user_id, page, limit)
    return [serialize_doc(chat) for chat in chats]