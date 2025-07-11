from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI is not set. Please check your environment variables.")

client = AsyncIOMotorClient(MONGO_URI)

db = client["chatdb"] 

async def init_indexes():
    await db.chats.create_index([("user_id", ASCENDING)])
    await db.chats.create_index([("conversation_id", ASCENDING)])
    await db.chats.create_index([("timestamp", ASCENDING)])
    await db.users.create_index([("email", ASCENDING)], unique=True)
