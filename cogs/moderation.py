from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'✅ {member.mention} تم طرده. السبب: {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'✅ {member.mention} تم حظره. السبب: {reason}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, minutes: int = 10):
        guild = ctx.guild
        muted = discord.utils.get(guild.roles, name='Muted')
        if muted is None:
            muted = await guild.create_role(name='Muted')
            for ch in guild.channels:
                await ch.set_permissions(muted, send_messages=False, speak=False)
        await member.add_roles(muted)
        await ctx.send(f'🔇 {member.mention} تم اكتماله لمدة {minutes} دقيقة.')
        await ctx.send('سأرفع الصمت تلقائياً بعد المدة.')
        await discord.utils.sleep_until(None)  # placeholder, not to block

async def setup(bot):
    await bot.add_cog(Moderation(bot))
