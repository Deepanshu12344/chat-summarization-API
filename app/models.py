from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class ChatCreate(BaseModel):
    sender_id: str
    receiver_id: str
    message: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)
    seen: bool = False


class UserCreate(BaseModel):
    username: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=6, max_length=128, description="Password (min 6 chars)")
    friends: List[str]= []
    pending_requests: List[str] = []
    sent_requests: List[str] = []

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=6, max_length=128, description="Password (min 6 chars)")

class UserResponse(BaseModel):
    username: Optional[str]
    email: EmailStr

    class Config:
        from_attributes = True


class SummarizeRequest(BaseModel):
    conversation_id: str

class SummaryResponse(BaseModel):
    summary: str