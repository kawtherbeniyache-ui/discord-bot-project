import discord
from discord.ext import commands
import yt_dlp as youtube_dl

# إعدادات yt-dlp
ytdl_format_options = {
    'format': 'bestaudio/best',
    'quiet': True,
    'noplaylist': True,
    'extract_flat': 'in_playlist'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # أمر دخول القناة الصوتية
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f"✅ دخلت القناة الصوتية: {channel}")
        else:
            await ctx.send("❌ أنت لست في أي قناة صوتية!")

    # أمر الخروج من القناة
    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("✅ خرجت من القناة الصوتية!")
        else:
            await ctx.send("❌ البوت ليس في أي قناة صوتية!")

    # أمر تشغيل الموسيقى
    @commands.command()
    async def play(self, ctx, url):
        # التأكد أن البوت داخل القناة الصوتية
        if not ctx.voice_client:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                return await ctx.send("❌ أنت لست في أي قناة صوتية!")

        vc = ctx.voice_client

        # تحميل رابط الموسيقى
        info = ytdl.extract_info(url, download=False)
        url2 = info['url']
        source = discord.FFmpegPCMAudio(url2, **ffmpeg_options)
        vc.play(source)
        await ctx.send(f"▶️ الآن يتم تشغيل: {info['title']}")

# تحميل الكوج عند استدعاء البوت
async def setup(bot):
    await bot.add_cog(Music(bot))
