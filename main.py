from pyrogram import Client
import config

app = Client(
    "my_userbot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins=dict(root="destinyxsparsh/plugins")
)

if __name__ == "__main__":
    print("Bot starting...")
    app.run()
