from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class ChatCreate(BaseModel):
    message: str
    sender_email: EmailStr
    receiver_email: EmailStr
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)

class SummarizeRequest(BaseModel):
    conversation_id: str

class SummaryResponse(BaseModel):
    summary: str

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=6, max_length=128, description="Password (min 6 chars)")
    friends: List[str]= []
    pending_requests: List[str] = []
    sent_requests: List[str] = []
    messageId: List[str] = [] 

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=6, max_length=128, description="Password (min 6 chars)")

class UserResponse(BaseModel):
    name: Optional[str]
    email: EmailStr

    class Config:
        orm_mode = True