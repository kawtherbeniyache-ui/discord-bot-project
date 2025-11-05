import random
from discord.ext import commands

# قائمة الفوازير
RIDDLES = [
    ('ما هو الشيء الذي كلما زاد نقص؟', 'العمر'),
    ('له أوراق وليس شجرة، ما هو؟', 'الكتاب'),
    ('ما الشيء الذي يكتب ولا يقرأ؟', 'القلم'),
    ('شيء إذا أخذت منه كبر، ما هو؟', 'الحفرة'),
    ('ما هو الشيء الذي يمشي بلا رجلين؟', 'الوقت'),
]

class Riddles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_riddles = {}  # لحفظ الفزورة الحالية لكل مستخدم

    @commands.command(name='riddle2')  # اسم فريد لتجنب التعارض
    async def riddle(self, ctx):
        q, a = random.choice(RIDDLES)
        self.active_riddles[ctx.author.id] = a.lower()
        await ctx.send(f"🧩 فزورة لك يا {ctx.author.mention}:\n**{q}**\nاكتب `!riddle_answer <جوابك>` للإجابة 👇")

    @commands.command(name='riddle_answer')  # اسم مختلف عن أي كوج آخر
    async def answer(self, ctx, *, guess: str):
        correct_answer = self.active_riddles.get(ctx.author.id)
        if not correct_answer:
            return await ctx.send("❌ ما عندك فزورة حالياً! اكتب `!riddle2` لتبدأ واحدة جديدة.")

        if guess.lower().strip() == correct_answer:
            await ctx.send("✅ إجابة صحيحة! أحسنت 👏")
            del self.active_riddles[ctx.author.id]
        else:
            await ctx.send("❌ إجابة خاطئة! حاول مرة ثانية 😅")

async def setup(bot):
    await bot.add_cog(Riddles(bot))
