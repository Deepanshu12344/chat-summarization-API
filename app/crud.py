from app.database import db
from app.models import ChatCreate
from bson.objectid import ObjectId

async def insert_chat(chat: ChatCreate):
    return await db.chats.insert_one(chat.dict())

async def get_conversation(message_id: str):
    return await db.chats.find({"_id": message_id}).to_list(1000)

async def delete_conversation(message_id: str):
    return await db.chats.delete_many({"_id": message_id})

async def get_user_chats(user_id: str, page: int, limit: int):
    skip = (page - 1) * limit
    return await db.chats.find({"user_id": user_id}).skip(skip).limit(limit).to_list(length=limit)