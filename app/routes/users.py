from fastapi import APIRouter
from app.crud import get_user_chats

router = APIRouter()

@router.get("/users/{user_id}/chats")
async def user_chats(user_id: str, page: int = 1, limit: int = 10):
    chats = await get_user_chats(user_id, page, limit)
    return chats