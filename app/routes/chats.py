from fastapi import APIRouter, HTTPException, Depends, Query, Body
from app.models import ChatCreate, SummarizeRequest, SummaryResponse
from app.crud import insert_chat, get_conversation, delete_conversation
from app.llm_utils import summarize_chat, analyze_conversation
from app.database import db
from app.controllers.chats import chat_with_friend, get_message
from app.middleware.dependencies import get_current_user_email
from bson import ObjectId

def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

router = APIRouter()


@router.post("/send_msg")
async def send_message(
    receiver_username: str = Query(...),
    message: str = Body(..., embed=True),
    current_user_email: str = Depends(get_current_user_email)
):
    sender = await db.users.find_one({"email": current_user_email})
    if not sender:
        raise HTTPException(status_code=404, detail="Sender not found")

    sender_username = sender.get("username")
    return await chat_with_friend(sender_username, receiver_username, message)


@router.get("/get_msg")
async def recv_msg(
    receiver_username: str = Query(...),
    current_user_email: str = Depends(get_current_user_email)
):
    sender = await db.users.find_one({"email": current_user_email})
    if not sender:
        raise HTTPException(status_code=404, detail="Sender not found")

    sender_username = sender.get("username")
    return await get_message(sender_username, receiver_username)