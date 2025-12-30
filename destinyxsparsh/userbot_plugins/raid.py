import asyncio
from pyrogram import Client, filters

@Client.on_message(filters.command("raid", ".") & filters.me)
async def raid_cmd(client, message):
    args = message.text.split()
    if len(args) < 3:
        return await message.edit("❌ **Usage:** `.raid [count] [message]` (Reply to user)")
    
    count = int(args[1])
    spam_msg = " ".join(args[2:])
    
    if not message.reply_to_message:
        return await message.edit("❌ Please reply to the victim's message.")

    target = message.reply_to_message.from_user.id
    await message.delete()

    for _ in range(count):
        await client.send_message(target, spam_msg)
        await asyncio.sleep(0.3)
