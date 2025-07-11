from app.models import UserCreate
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from database import db
from pymongo.errors import DuplicateKeyError
from passlib.hash import bcrypt

async def register(user:UserCreate):
    #check existing user
    existing_user = await db.users.find_one({"email":user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered" 
        )
    
    #Hash password
    user_dict = user.dict()
    user_dict["password"] = bcrypt.hash(user.password)

    try:
        result = await db.users.insert_one(user_dict)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message":"User created successfully", "user_id": str(result.inserted_id)}
        )   
    except DuplicateKeyError as e: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this Email already exists" 
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong: " + str(e)
        )
    
async def login(user:UserCreate):
    