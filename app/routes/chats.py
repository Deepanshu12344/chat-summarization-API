from fastapi import APIRouter, HTTPException
from app.models import ChatCreate, SummarizeRequest, SummaryResponse
from app.crud import insert_chat, get_conversation, delete_conversation
from app.llm_utils import summarize_chat
from app.database import db
from bson import ObjectId

def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

router = APIRouter()

@router.post("/chats")
async def store_chat(chat: ChatCreate):
    await insert_chat(chat)
    return {"message": "Chat stored"}

@router.get("/chats/{conversation_id}")
async def get_conversation(conversation_id: str):
    docs = await db.chats.find({"conversation_id": conversation_id}).to_list(1000)
    return [serialize_doc(doc) for doc in docs]


@router.delete("/chats/{conversation_id}")
async def delete_chat(conversation_id: str):
    await delete_conversation(conversation_id)
    return {"message": "Conversation deleted"}

@router.post("/chats/summarize", response_model=SummaryResponse)
async def summarize(request: SummarizeRequest):
    chat = await get_conversation(request.conversation_id)
    messages = [c["message"] for c in chat]
    summary = await summarize_chat(messages)
    return {"summary": summary}