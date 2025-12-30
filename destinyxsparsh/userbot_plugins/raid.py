import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

@Client.on_message(filters.command("raid", ".") & filters.me)
async def raid_cmd(client, message):
    # Command ko parts mein todna
    text_parts = message.text.split(None, 2)
    
    # Check: .raid [count] [message]
    if len(text_parts) < 3 or not message.reply_to_message:
        return await message.edit("❌ **Usage:** `.raid [count] [message]` (Reply to someone)")

    try:
        count = int(text_parts[1])
        spam_msg = text_parts[2]
    except ValueError:
        return await message.edit("❌ Count ek number hona chahiye (e.g. .raid 5 hi)")

    target = message.reply_to_message.from_user.id
    
    # Command message delete karna
    await message.delete()

    for i in range(count):
        try:
            await client.send_message(target, spam_msg)
            # 0.3 sec gap taaki Telegram account ban na kare
            await asyncio.sleep(0.3) 
        except FloodWait as e:
            # Agar Telegram bohot fast bhejte hue rok de
            await asyncio.sleep(e.value)
        except Exception:
            break
