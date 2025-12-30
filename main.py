import asyncio
from pyrogram import Client
from config import Config
from destinyxsparsh.database.db import get_all_sessions

async def main():
    # 1. Main Master Account ko start karna
    master_bot = Client(
        "MasterBot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        session_string=Config.STRING_SESSION,
        plugins=dict(root="destinyxsparsh/plugins")
    )
    await master_bot.start()
    print("✅ Master Bot Started!")

    # 2. Database se saare saved sessions load karna
    saved_sessions = await get_all_sessions()
    for i, session in enumerate(saved_sessions):
        try:
            extra_client = Client(
                name=f"Userbot_{i}",
                api_id=Config.API_ID,
                api_hash=Config.API_HASH,
                session_string=session,
                plugins=dict(root="destinyxsparsh/plugins")
            )
            await extra_client.start()
            print(f"✅ Extra Client {i+1} Started!")
        except Exception as e:
            print(f"❌ Could not start session {i+1}: {e}")

    # Bot ko chalu rakhne ke liye
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
