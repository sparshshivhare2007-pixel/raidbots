from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

if Config.MONGO_URL:
    mongo = AsyncIOMotorClient(Config.MONGO_URL)
    db = mongo.destinybot
else:
    db = None

# Aap yahan users ya settings save karne ke functions likh sakte hain
