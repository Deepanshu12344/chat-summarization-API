from app.models import UserCreate, UserLogin
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.database import db
from pymongo.errors import DuplicateKeyError
from datetime import datetime, timedelta
from passlib.hash import bcrypt
import jwt
from app.utils.auth import create_access_token


JWT_SECRET = "your_jwt_secret"
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_MINUTES = 60


# Register
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
    user_dict["friends"] = []

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


# Login
async def login(user: UserLogin):
    # Check if user exists
    existing_user = await db.users.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist"
        )

    # Verify password
    if not bcrypt.verify(user.password, existing_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect Password"
        )

    # Create JWT token
    access_token = create_access_token({"sub": user.email})

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }