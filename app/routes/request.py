from fastapi import APIRouter, Depends
from app.controllers.request import send_friend_request, accept_friend_request
from app.middleware.dependencies import get_current_user_email


router = APIRouter()

@router.post("/send_req")
async def send_request(receiver_email: str, current_user_email: str = Depends(get_current_user_email)):
    return await send_friend_request(current_user_email, receiver_email)

@router.post("/accept_req")
async def send_request(receiver_email: str, current_user_email: str = Depends(get_current_user_email)):
    return await accept_friend_request(current_user_email, receiver_email)

