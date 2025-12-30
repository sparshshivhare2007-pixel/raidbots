# ⚡ DestinyXSparsh Multi-Userbot ⚡

A powerful Telegram Multi-Session Userbot manager that allows you to host multiple userbot accounts via an Assistant Bot.

---

## 🚀 Features
- **Multi-Session:** Add multiple accounts using string sessions.
- **Database Support:** MongoDB integrated to keep sessions alive after restart.
- **Raid Command:** Professional raid module for the userbots.
- **Assistant Bot:** Control everything through a simple bot interface.

---

## 🛠 Setup & Deployment

### 1. Requirements
* `API_ID` & `API_HASH`: Get from [my.telegram.org](https://my.telegram.org).
* `BOT_TOKEN`: Get from [@BotFather](https://t.me/BotFather).
* `MONGO_URL`: Get from [MongoDB Atlas](https://www.mongodb.com/).
* `OWNER_ID`: Your Telegram User ID.

### 2. Deploy to Heroku
Click the button below to deploy directly to Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME)

> **Note:** Replace `YOUR_GITHUB_USERNAME/YOUR_REPO_NAME` in the link above with your actual GitHub details.

---

## 📝 Commands

### Assistant Bot Commands (Token Bot)
| Command | Description |
| :--- | :--- |
| `/start` | Check if the bot is alive |
| `/add [session]` | Add a new Userbot via String Session |

### Userbot Commands (Your Account)
| Command | Description |
| :--- | :--- |
| `.ping` | Check Userbot speed |
| `.raid [count] [message]` | Start a raid (Reply to a user) |

---

## ⚠️ Disclaimer
This project is for educational purposes only. Using userbots can lead to account bans if misused. The developer is not responsible for any misuse.

## 🤝 Support
For any help, join the support channel.
