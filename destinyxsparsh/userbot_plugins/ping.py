import time
from pyrogram import Client, filters

@Client.on_message(filters.command("ping", ".") & filters.me)
async def ping_cmd(client, message):
    start = time.time()
    # Pehle message ko edit karke response check karte hain
    await message.edit("🏓 **Pinging...**")
    end = time.time()
    
    # Speed calculate karna
    delta_ms = (end - start) * 1000
    
    # Final reply
    await message.edit(
        f"🚀 **Pong!**\n"
        f"✨ **Speed:** `{delta_ms:.2f} ms`\n"
        f"👤 **Master:** {client.me.first_name}"
    )
