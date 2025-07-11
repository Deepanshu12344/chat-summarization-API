from fastapi import APIRouter, Depends
from app.crud import get_user_chats
from typing import List
from app.controllers.users import fetch_all_users_except_current 
from app.models import UserResponse
from app.middleware.dependencies import get_current_user_email

router = APIRouter(prefix="/users")

@router.get("/{user_id}/chats")
async def user_chats(user_id: str, page: int = 1, limit: int = 10):
    chats = await get_user_chats(user_id, page, limit)
    return chats

@router.get("/all", response_model=List[UserResponse])
async def all_users(current_user_email: str = Depends(get_current_user_email)):
    return await fetch_all_users_except_current(current_user_email)
