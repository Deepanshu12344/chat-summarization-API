from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["chatdb"]

async def init_indexes():
    await db.chats.create_index([("user_id", ASCENDING)])
    await db.chats.create_index([("conversation_id", ASCENDING)])
    await db.chats.create_index([("timestamp", ASCENDING)])
