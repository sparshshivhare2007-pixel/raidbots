from motor.motor_asyncio import AsyncIOMotorClient
import os

# Heroku Config Vars se Mongo URL uthayein
MONGO_URL = os.getenv("MONGO_URL", "")
db = AsyncIOMotorClient(MONGO_URL).DestinyDB
sessions_col = db.sessions # Collection ka naam
