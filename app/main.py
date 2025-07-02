from fastapi import FastAPI
from app.routes import chats, users
from app.database import init_indexes


app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "Chat Summarization API is running",
        "docs": "/docs",
        "endpoints": ["/chats", "/users"]
    }
@app.on_event("startup")
async def startup():
    await init_indexes()

app.include_router(chats.router)
app.include_router(users.router)

