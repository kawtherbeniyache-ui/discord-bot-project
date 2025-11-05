from discord.ext import commands
import discord

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say')
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message: str):
        """
        يسمح للأدمن بكتابة نص وسيقوم البوت بنشره باسم البوت.
        مثال:
        !say مرحباً بالجميع
        """
        await ctx.message.delete()
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Say(bot))
