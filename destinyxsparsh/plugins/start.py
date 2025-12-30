from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.me)
async def start_command(client, message):
    image_url = "https://files.catbox.moe/gnzkrj.jpg" # Apni image ka link yahan dalein
    
    text = (
        "**🔥 DestinyXSparsh Userbot Active!**\n\n"
        "Ye bot ab puri tarah setup hai.\n"
        "Aap niche diye gaye buttons use kar sakte hain."
    )
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support Group", url="https://t.me/PEACE_CHATTING_WORLD"),
            InlineKeyboardButton("Updates", url="https://t.me/peaceXbots")
        ],
        [
            InlineKeyboardButton("Owner", url="https://t.me/you")
        ]
    ])

    # Image ke sath message bhejna
    await client.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption=text,
        reply_markup=buttons
    )
