from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

# MongoDB Connection
if Config.MONGO_URL:
    client = AsyncIOMotorClient(Config.MONGO_URL)
    db = client.DestinyDB
    sessions_db = db.sessions
else:
    print("❌ ERROR: MONGO_URL not found in Config!")
    sessions_db = None

# Function: Database mein session save karne ke liye
async def add_session_to_db(user_id, session_str):
    if sessions_db is not None:
        await sessions_db.update_one(
            {"user_id": user_id},
            {"$set": {"session": session_str}},
            upsert=True
        )
        return True
    return False

# Function: Saare saved sessions nikaalne ke liye
async def get_all_sessions():
    sessions = []
    if sessions_db is not None:
        async for doc in sessions_db.find():
            sessions.append(doc["session"])
    return sessions

# Function: Session delete karne ke liye (agar logout karna ho)
async def remove_session_from_db(user_id):
    if sessions_db is not None:
        await sessions_db.delete_one({"user_id": user_id})
        return True
    return False
