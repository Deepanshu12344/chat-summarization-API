from app.database import db
from fastapi import HTTPException
from app.models import ChatCreate
from app.crud import insert_chat


async def chat_with_friend(sender_email:str, receiver_email:str, chat:ChatCreate):
    try: 
        receiver = await db.users.find_one({"email":receiver_email})
        sender = await db.users.find_one({"email":sender_email})

        if not receiver or not sender:
            raise HTTPException(
                status_code=400,
                detail="user not exist"
            )
        
        if sender_email not in receiver.get("friends",[]):
            raise HTTPException(
                status_code=400,
                detail="not friends"
            )
        
        message = await insert_chat(chat)
        message_id = str(message.inserted_id)
        
        await db.users.update_one({"email": receiver_email}, {"$push":{"messageId":message_id}})
        await db.users.update_one({"email": sender_email}, {"$push":{"messageId":message_id}})

        return {
            "message":"message sent successfully",
            "data": message
        }
    except Exception as e:
        return {f"message":"system error i.e {e}"}