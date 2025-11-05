import discord
from discord.ext import commands
import json

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('config.json', 'r', encoding='utf-8') as f:
            self.cfg = json.load(f)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # DM welcome
        try:
            await member.send(f'أهلاً {member.name}! مرحباً بك في السيرفر.')
        except Exception:
            pass

        # Channel welcome if configured
        channel_id = self.cfg.get('welcome_channel')
        if channel_id:
            channel = member.guild.get_channel(int(channel_id))
            if channel:
                await channel.send(f'أهلاً وسهلاً {member.mention} — رحبوا به!')

async def setup(bot):
    await bot.add_cog(Welcome(bot))
