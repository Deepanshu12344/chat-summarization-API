from fastapi import APIRouter, Depends, HTTPException
from app.controllers.request import send_friend_request, accept_friend_request
from app.middleware.dependencies import get_current_user_email
from app.database import db  

router = APIRouter()

@router.post("/send_req")
async def send_request(receiver_username: str, current_user_email: str = Depends(get_current_user_email)):
    sender = await db.users.find_one({"email": current_user_email})
    if not sender:
        raise HTTPException(status_code=404, detail="Current user not found")

    sender_username = sender["username"]
    return await send_friend_request(sender_username, receiver_username)

@router.post("/accept_req")
async def accept_request(sender_username: str, current_user_email: str = Depends(get_current_user_email)):
    receiver = await db.users.find_one({"email": current_user_email})
    if not receiver:
        raise HTTPException(status_code=404, detail="Current user not found")

    receiver_username = receiver["username"]
    return await accept_friend_request(sender_username, receiver_username)
