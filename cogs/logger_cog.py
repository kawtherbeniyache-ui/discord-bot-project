from discord.ext import commands
import logging
import os

class LoggerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        os.makedirs('logs', exist_ok=True)
        self.msg_logger = logging.getLogger('messages')
        handler = logging.FileHandler(filename='logs/messages.log', encoding='utf-8', mode='a')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))
        if not self.msg_logger.handlers:
            self.msg_logger.addHandler(handler)
        self.msg_logger.setLevel(logging.INFO)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        self.msg_logger.info(f'{message.guild} | {message.author} : {message.content}')

async def setup(bot):
    await bot.add_cog(LoggerCog(bot))
