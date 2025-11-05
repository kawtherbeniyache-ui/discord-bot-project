import json
import logging
import os
import asyncio
from discord.ext import commands
import discord

# Load config
with open('config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

TOKEN = cfg.get('token')
PREFIX = cfg.get('prefix', '!')
INTENTS = discord.Intents.default()
INTENTS.members = True
INTENTS.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='logs/bot.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Auto-load cogs
if __name__ == '__main__':
    import asyncio

    async def load_cogs():
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not filename.startswith('__'):
                try:
                    await bot.load_extension(f'cogs.{filename[:-3]}')
                    print(f'Loaded cog: {filename}')
                except Exception as e:
                    print(f'Failed to load {filename}:', e)

    async def main():
        os.makedirs('logs', exist_ok=True)
        await load_cogs()

        if TOKEN == '' or not TOKEN:
            print('Please set your token في config.json قبل تشغيل البوت.')
        else:
            await bot.start(TOKEN)

    asyncio.run(main())