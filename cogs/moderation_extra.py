from discord.ext import commands
import discord

class ModerationExtra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount < 1:
            return await ctx.send("❌ يرجى إدخال عدد صحيح أكبر من 0.")
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f'🧹 تم مسح {len(deleted)} رسالة.', delete_after=5)

async def setup(bot):
    await bot.add_cog(ModerationExtra(bot))
