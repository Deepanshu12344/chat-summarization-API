from app.database import db
from fastapi import HTTPException
from app.models import ChatCreate
from app.crud import insert_chat


async def chat_with_friend(sender_email:str, receiver_email:str, chat:ChatCreate):
    receiver = await db.users.find_one({"email":receiver_email})
    sender = await db.users.find_one({"email":sender_email})

    if not receiver or not sender:
        raise HTTPException(
            status_code=400,
            detail="user not exist"
        )
    
    await insert_chat(chat)
    return {"message":"message sent"}
