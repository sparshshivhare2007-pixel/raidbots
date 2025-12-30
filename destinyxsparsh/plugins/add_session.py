from pyrogram import Client, filters
from destinyxsparsh.database.db import sessions_col

# Dictionary taaki hum running clients ko track kar sakein
running_clients = {}

@Client.on_message(filters.command("add") & filters.me)
async def add_session(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/add [string_session]`")

    session_str = message.text.split(None, 1)[1]
    
    try:
        # Check karna ki session valid hai ya nahi
        new_client = Client(
            name="userbot_session",
            api_id=client.api_id,
            api_hash=client.api_hash,
            session_string=session_str
        )
        
        await new_client.start()
        user = await new_client.get_me()
        
        # Database mein save karna
        await sessions_col.update_one(
            {"user_id": user.id},
            {"$set": {"session": session_str}},
            upsert=True
        )
        
        running_clients[user.id] = new_client
        await message.reply(f"✅ **Connected:** {user.first_name}\nAb ye account commands accept karega.")
        
    except Exception as e:
        await message.reply(f"❌ **Error:** {str(e)}")
