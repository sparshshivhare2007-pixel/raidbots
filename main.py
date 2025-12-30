import asyncio
from pyrogram import Client, idle
from config import Config
from destinyxsparsh.database.db import get_all_sessions

async def start_bot():
    # 1. Start Assistant Bot
    bot = Client(
        "Assistant",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="destinyxsparsh/plugins")
    )
    
    await bot.start()
    print("✅ Assistant Bot Online!")

    # 2. Load all Userbots from Database
    sessions = await get_all_sessions()
    for sess in sessions:
        try:
            ubot = Client(
                name=f"ubot_{sess[:10]}",
                api_id=Config.API_ID,
                api_hash=Config.API_HASH,
                session_string=sess,
                plugins=dict(root="destinyxsparsh/userbot_plugins")
            )
            await ubot.start()
            print(f"✅ Userbot {ubot.me.first_name} Active!")
        except Exception as e:
            print(f"❌ Error loading session: {e}")

    # Bot ko chalu rakhne ke liye idle use karein
    await idle()
    
    # Jab bot stop ho toh saare connections band karein
    await bot.stop()

if __name__ == "__main__":
    # Modern way to run asyncio in Python 3.10+
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
