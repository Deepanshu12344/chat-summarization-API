from fastapi import APIRouter, Depends, HTTPException, status
from app.models import UserCreate, UserLogin
from app.controllers.auth import register, login 

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    return await register(user)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(user: UserLogin):
    return await login(user)
