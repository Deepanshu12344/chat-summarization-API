from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ChatCreate(BaseModel):
    user_id: str
    conversation_id: str
    message: str
    sender: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Chat(ChatCreate):
    id: str

class SummarizeRequest(BaseModel):
    conversation_id: str

class SummaryResponse(BaseModel):
    summary: str