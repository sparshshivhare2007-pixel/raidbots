from pyrogram import Client, filters
from destinyxsparsh.database.db import add_session_to_db
from config import Config

@Client.on_message(filters.command("add") & filters.user(Config.OWNER_ID))
async def add_session(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ **Format:** `/add [string_session]`")

    session_str = message.text.split(None, 1)[1]
    wait = await message.reply("⏳ **Connecting Userbot...**")

    try:
        new_ub = Client("temp", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=session_str)
        await new_ub.start()
        user = await new_ub.get_me()
        await add_session_to_db(user.id, session_str)
        await wait.edit(f"✅ **{user.first_name}** is now a live Userbot!")
        # Restart is usually needed to load plugins for new client
    except Exception as e:
        await wait.edit(f"❌ **Error:** `{e}`")
