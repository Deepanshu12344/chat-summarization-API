from app.models import UserCreate, UserLogin
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.database import db
from pymongo.errors import DuplicateKeyError
from datetime import datetime, timedelta
from passlib.hash import bcrypt
import jwt


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
async def login(user:UserLogin):
    #check existing user
    existing_user = await db.users.find_one({"email":user.email})
    if not existing_user:
        raise HTTPException(
            status_code=400,
            detail="User does not exist"
        )
    #verify password
    if not bcrypt.verify(user.password, existing_user["password"]):
        raise HTTPException(
            status_code=400,
            detail="Incorrect Password"
        )
    
    # Create JWT payload
    payload = {
        "sub": user.email,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXP_DELTA_MINUTES)
    }

    # Encode token
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }
