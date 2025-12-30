from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    image_url = "https://files.catbox.moe/gnzkrj.jpg"
    
    text = (
        "**🔥 DestinyXSparsh Userbot Active!**\n\n"
        "Main aapka Assistant Bot hoon. Apne account ko Userbot banane ke liye niche di gayi command use karein:\n\n"
        "➡️ `/add [String_Session]`"
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

    await client.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption=text,
        reply_markup=buttons
    )
