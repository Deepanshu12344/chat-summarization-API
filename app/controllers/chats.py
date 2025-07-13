from app.database import db
from fastapi import HTTPException
from app.models import ChatCreate
from app.crud import insert_chat, get_conversation

def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

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
            "message": "Message sent successfully",
            "message_id": message_id,
            "sender": sender_email,
            "receiver": receiver_email
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"System error: {str(e)}"
        )


async def get_message(sender_email:str, receiver_email:str):
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
        messages = await db.chats.find({
            "$or":[
                {"sender_email": sender_email, "receiver_email": receiver_email},
                {"sender_email": receiver_email, "receiver_email": sender_email}
            ]
        }).sort("'timestamp", 1).to_list(length=None)
        for msg in messages:
            msg["id"] = str(msg["_id"])
            del msg["_id"]

        return {"chat_history": messages}
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"System error: {str(e)}"
        )
