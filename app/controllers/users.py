from app.models import UserCreate
from app.database import db
from fastapi import HTTPException

#get all users except oneself
async def fetch_all_users_except_current(current_user_email:str):
    try:
        users = await db.users.find({"email": {"$ne": current_user_email}}).to_list(length=None)

        for user in users:
            user["_id"] = str(user["_id"])
            user.pop("password",None)

        return users
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching users:{str(e)}"
        )
    
