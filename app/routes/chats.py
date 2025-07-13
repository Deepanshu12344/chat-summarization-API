from fastapi import APIRouter, HTTPException, Depends, Query
from app.models import ChatCreate, SummarizeRequest, SummaryResponse
from app.crud import insert_chat, get_conversation, delete_conversation
from app.llm_utils import summarize_chat, analyze_conversation
from app.database import db
from app.controllers.chats import chat_with_friend
from app.middleware.dependencies import get_current_user_email
from bson import ObjectId

def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

router = APIRouter()

@router.post("/send_msg")
async def send_message(receiver_email: str = Query(...),  chat: ChatCreate = ..., current_user_email: str = Depends(get_current_user_email)):
    return await chat_with_friend(current_user_email, receiver_email, chat)

# @router.post("/chats")
# async def store_chat(chat: ChatCreate):
#     await insert_chat(chat)
#     return {"message": "Chat stored"}

# @router.get("/chats/{conversation_id}")
# async def get_conversation(conversation_id: str):   
#     docs = await db.chats.find({"conversation_id": conversation_id}).to_list(1000)
#     return [serialize_doc(doc) for doc in docs]


# @router.delete("/chats/{conversation_id}")
# async def delete_chat(conversation_id: str):
#     await delete_conversation(conversation_id)
#     return {"message": "Conversation deleted"}

# @router.post("/chats/summarize", response_model=SummaryResponse)
# async def summarize(request: SummarizeRequest):
#     chat = await get_conversation(request.conversation_id)
#     messages = [c["message"] for c in chat]
#     summary = await summarize_chat(messages)
#     return {"summary": summary}

# @router.post("/chats/analyze", response_model=SummaryResponse)
# async def analyze(request: SummarizeRequest):
#     chat = await get_conversation(request.conversation_id)
#     messages = [c["message"] for c in chat]
#     analysis = await analyze_conversation(messages)
#     return {"summary": analysis}