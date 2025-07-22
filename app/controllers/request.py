from fastapi import HTTPException
from app.database import db

from fastapi import HTTPException

async def send_friend_request(sender_username: str, receiver_username: str):
    try:
        if sender_username == receiver_username:
            raise HTTPException(
                status_code=400,
                detail="You can't send a friend request to yourself"
            )

        sender = await db.users.find_one({"username": sender_username})
        receiver = await db.users.find_one({"username": receiver_username})

        if not sender or not receiver:
            raise HTTPException(status_code=404, detail="User not found")

        # Use username (or ID) strings for list checks
        if sender_username in receiver.get("pending_requests", []):
            raise HTTPException(status_code=400, detail="Request already sent")

        if sender_username in receiver.get("friends", []):
            raise HTTPException(status_code=400, detail="Already friends")

        # Update both users
        await db.users.update_one(
            {"username": receiver_username},
            {"$push": {"pending_requests": sender_username}}
        )

        await db.users.update_one(
            {"username": sender_username},
            {"$push": {"sent_requests": receiver_username}}
        )

        return {"message": "Friend request sent successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"System error: {str(e)}"
        )


from fastapi import HTTPException

async def accept_friend_request(sender_username: str, receiver_username: str):
    try:
        # Step 1: Validate users
        sender = await db.users.find_one({"username": sender_username})
        receiver = await db.users.find_one({"username": receiver_username})

        if not sender or not receiver:
            raise HTTPException(status_code=404, detail="User not found")

        # Step 2: Check if the request exists
        if sender_username not in receiver.get("pending_requests", []):
            raise HTTPException(status_code=400, detail="No friend request to accept")

        # Step 3: Check if already friends
        if sender_username in receiver.get("friends", []):
            raise HTTPException(status_code=400, detail="Already friends")

        # Step 4: Update both users
        await db.users.update_one(
            {"username": receiver_username},
            {
                "$pull": {"pending_requests": sender_username},
                "$push": {"friends": sender_username}
            }
        )

        await db.users.update_one(
            {"username": sender_username},
            {
                "$pull": {"sent_requests": receiver_username},
                "$push": {"friends": receiver_username}
            }
        )

        return {"message": "Friend request accepted successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"System error: {str(e)}"
        )
