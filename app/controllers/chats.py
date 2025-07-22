from app.database import db
from fastapi import HTTPException
from app.models import ChatCreate
from app.crud import insert_chat

def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

async def chat_with_friend(sender_username: str, receiver_username: str, message: str):
    try:
        if sender_username == receiver_username:
            raise HTTPException(
                status_code=400,
                detail="You can't chat with yourself"
            )

        sender = await db.users.find_one({"username": sender_username})
        receiver = await db.users.find_one({"username": receiver_username})

        if not sender or not receiver:
            raise HTTPException(status_code=404, detail="User not found")
        
        if sender_username not in receiver.get("friends", []):
            raise HTTPException(
                status_code=400,
                detail="You are not friends with this user"
            )

        chat = ChatCreate(
            sender_id=str(sender["_id"]),
            receiver_id=str(receiver["_id"]),
            message=message
        )
        
        chat_doc = await insert_chat(chat)
        inserted_chat = await db.chats.find_one({"_id": chat_doc.inserted_id})
        return serialize_doc(inserted_chat)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"System error: {str(e)}"
        )


async def get_message(sender_username: str, receiver_username: str):
    try:
        receiver = await db.users.find_one({"username": receiver_username})
        sender = await db.users.find_one({"username": sender_username})

        if not receiver or not sender:
            raise HTTPException(
                status_code=400,
                detail="User not found"
            )

        if sender_username not in receiver.get("friends", []):
            raise HTTPException(
                status_code=400,
                detail="You are not friends with this user"
            )

        messages = await db.chats.find({
            "$or": [
                {"sender_id": str(sender["_id"]), "receiver_id": str(receiver["_id"])},
                {"sender_id": str(receiver["_id"]), "receiver_id": str(sender["_id"])}
            ]
        }).sort("timestamp", 1).to_list(length=None)

        for msg in messages:
            msg["id"] = str(msg["_id"])
            del msg["_id"]

        return {"chat_history": messages}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"System error: {str(e)}"
        )

