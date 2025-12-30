import asyncio
from pyrogram import Client, filters

@Client.on_message(filters.command("raid", ".") & filters.me)
async def raid_cmd(client, message):
    # Format: .raid 5 @username Hello
    args = message.text.split(None, 3)
    
    if len(args) < 4:
        await message.edit("Format: `.raid 5 @username message`")
        return

    count = int(args[1])
    target = args[2]
    spam_msg = args[3]

    await message.edit(f"🚀 **Raid Starting on {target}...**")
    await asyncio.sleep(1)
    await message.delete()

    for _ in range(count):
        await client.send_message(target, spam_msg)
        await asyncio.sleep(0.3) # Flood se bachne ke liye
