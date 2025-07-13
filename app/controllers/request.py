from fastapi import HTTPException
from app.database import db

async def send_friend_request(sender_email:str, receiver_email:str):
    try:
        if sender_email == receiver_email:
            raise HTTPException(
                status_code=400,
                detail="You can't send friend request to yourself"
            )
        
        sender = await db.users.find_one({"email":sender_email})
        receiver = await db.users.find_one({"email":receiver_email})

        if not sender or not receiver:
            raise HTTPException(
                status_code=400,
                detail="User not found"
            )
        
        if sender in receiver.get("pending_requests", []):
            raise HTTPException(
                status_code=400,
                detail="Request sent already"
            )
        
        if sender in receiver.get("friends", []):
            raise HTTPException(
                status_code=400,
                detail="Already friends"
            )
        
        await db.users.update_one({"email": receiver_email}, {"$push":{"pending_requests":sender_email}})
        await db.users.update_one({"email": sender_email}, {"$push":{"sent_requests":receiver_email}})

        return {"message":"Request sent"}
    except Exception as e:
        return {f"message":"system error i.e {e}"}


async def accept_friend_request(sender_email:str, receiver_email:str):
    try:
        sender = await db.users.find_one({"email":sender_email})
        receiver = await db.users.find_one({"email":receiver_email})

        if sender_email not in receiver.get("pending_requests", []):
            raise HTTPException(
                status_code=400,
                detail="No request to accept"
            )

        if not sender or not receiver:
            raise HTTPException(
                status_code=400,
                detail="User not found"
            )
        
        if sender_email in receiver.get("friends", []):
            raise HTTPException(
                status_code=400,
                detail="Already friends"
            )
        
        await db.users.update_one(
            {"email": receiver_email}, 
            {"$pull": {"pending_requests": sender_email}, "$push":{"friends":sender_email}})
        
        await db.users.update_one(
            {"email": sender_email}, 
            {"$pull": {"sent_requests": receiver_email},"$push":{"friends":receiver_email}})
        
        return {"message": "Request Accepted"}
    except Exception as e:
        return {f"message":"system error i.e {e}"}