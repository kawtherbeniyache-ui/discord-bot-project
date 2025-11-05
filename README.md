Discord Server Bot (Python)
==========================

What this project includes
- Welcome messages (DM + channel)
- Basic moderation (kick/ban/mute + check perms)
- Small games: coinflip, rock-paper-scissors
- Riddles/fawazeer command
- Simple logging to logs/messages.log
- Easy to configure: open config.json and replace "YOUR_TOKEN_HERE" with your bot token

Requirements
- Python 3.10+ recommended
- Install dependencies:
    pip install -r requirements.txt

How to run
1. Open this folder in VS Code.
2. Edit config.json: set "token" to your bot token and optionally set "welcome_channel" id.
3. (Optional) Create a role named "Muted" for mute functionality, or the bot will try to create it.
4. Run:
    python bot.py

Files
- bot.py            : Entry point
- config.json       : Put your bot token here
- cogs/*.py         : Separate cog files for features
- requirements.txt  : pip dependencies

Notes
- Keep your token secret. Do NOT share it or push it publicly.
- This is a starter template — feel free to extend and improve.
