import asyncio
from pyrogram import Client
from destinyxsparsh.database.db import sessions_col
from config import Config

async def load_all_sessions():
    main_app = Client("main_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.STRING_SESSION)
    await main_app.start()
    print("Main Bot Started!")

    # Database se saare sessions nikaalna
    cursor = sessions_col.find({})
    async for doc in cursor:
        try:
            extra_client = Client(
                name=str(doc["user_id"]),
                api_id=Config.API_ID,
                api_hash=Config.API_HASH,
                session_string=doc["session"],
                plugins=dict(root="destinyxsparsh/plugins")
            )
            await extra_client.start()
            print(f"Loaded session for user: {doc['user_id']}")
        except Exception as e:
            print(f"Failed to load {doc['user_id']}: {e}")

    await asyncio.Event().wait() # Bot ko running rakhne ke liye

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(load_all_sessions())
