from pyrogram import Client, filters
from destinyxsparsh.database.db import add_session

@Client.on_message(filters.command("add", ".") & filters.me)
async def add_userbot(client, message):
    if len(message.command) < 2:
        return await message.edit("❌ **Usage:** `.add [string_session]`")

    string_session = message.text.split(None, 1)[1]
    status_msg = await message.edit("⏳ **Checking Session...**")

    try:
        # Check karne ke liye ek naya temporary client
        temp_client = Client(
            name="temp_client",
            api_id=client.api_id,
            api_hash=client.api_hash,
            session_string=string_session
        )
        
        await temp_client.start()
        me = await temp_client.get_me()
        
        # Database mein save karna
        await add_session(me.id, string_session)
        
        await status_msg.edit(f"✅ **Account Added Successfully!**\n👤 **Name:** {me.first_name}\n🆔 **ID:** {me.id}")
        
        # Note: Naye account ko activate karne ke liye bot restart karna padega 
        # ya dynamic loading code likhna hoga.
        await temp_client.stop()

    except Exception as e:
        await status_msg.edit(f"❌ **Error:** `{e}`")
