import os

class Config:
    API_ID = int(os.getenv("API_ID", "12345"))
    API_HASH = os.getenv("API_HASH", "your_hash")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGO_URL = os.getenv("MONGO_URL")
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    START_IMG = os.getenv("START_IMG", "https://telegra.ph/file/your-image.jpg")
