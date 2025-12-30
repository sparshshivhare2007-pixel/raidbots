from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

client = AsyncIOMotorClient(Config.MONGO_URL)
db = client.DestinyDB
sessions_db = db.sessions

async def add_session_to_db(user_id, session_str):
    await sessions_db.update_one(
        {"user_id": user_id},
        {"$set": {"session": session_str}},
        upsert=True
    )

async def get_all_sessions():
    sessions = []
    async for doc in sessions_db.find():
        sessions.append(doc["session"])
    return sessions
