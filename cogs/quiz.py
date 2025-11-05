import random
from discord.ext import commands

# قائمة الأسئلة مع الخيارات والإجابة الصحيحة
TRIVIA_QUESTIONS = [
    {"question": "ما هي عاصمة فرنسا؟", "options": ["A) باريس", "B) لندن", "C) روما"], "answer": "A"},
    {"question": "أكبر كوكب في النظام الشمسي؟", "options": ["A) الأرض", "B) المشتري", "C) زحل"], "answer": "B"},
    {"question": "ما هو أسرع حيوان بري؟", "options": ["A) الفهد", "B) الحصان", "C) الأسد"], "answer": "A"},
    {"question": "ما هو أطول نهر في العالم؟", "options": ["A) النيل", "B) الأمازون", "C) المسيسيبي"], "answer": "A"},
]

class Quiz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_trivia = None
        self.scores = {}  # تخزين النقاط لكل لاعب
        self.quiz_active = False

    @commands.command(name="quiz_start")
    async def start_quiz(self, ctx):
        if self.quiz_active:
            return await ctx.send("❌ هناك اختبار جاري بالفعل.")
        self.quiz_active = True
        await ctx.send("🎉 بدأ اختبار Trivia! اكتب `!quiz_answer <حرف>` للإجابة.")
        await self.ask_question(ctx)

    async def ask_question(self, ctx):
        self.current_trivia = random.choice(TRIVIA_QUESTIONS)
        options_text = "\n".join(self.current_trivia["options"])
        await ctx.send(f"❓ سؤال: **{self.current_trivia['question']}**\n{options_text}")

    @commands.command(name="quiz_answer")
    async def answer(self, ctx, choice: str):
        if not self.quiz_active or not self.current_trivia:
            return await ctx.send("⚠️ لا يوجد سؤال جاري الآن. استخدم `!quiz_start` للبدء.")
        
        user = ctx.author
        if choice.upper() == self.current_trivia["answer"]:
            self.scores[user] = self.scores.get(user, 0) + 1
            await ctx.send(f"✅ إجابة صحيحة! {user.mention} لديك الآن {self.scores[user]} نقطة.")
        else:
            await ctx.send(f"❌ خطأ! الإجابة الصحيحة كانت: **{self.current_trivia['answer']}**")
        
        await self.ask_question(ctx)

    @commands.command(name="quiz_score")
    async def score(self, ctx):
        if not self.scores:
            return await ctx.send("📊 لا يوجد أي نقاط حتى الآن.")
        leaderboard = "\n".join([f"{user}: {points} نقطة" for user, points in self.scores.items()])
        await ctx.send(f"🏆 النتائج الحالية:\n{leaderboard}")

    @commands.command(name="quiz_end")
    async def end_quiz(self, ctx):
        if not self.quiz_active:
            return await ctx.send("⚠️ لا يوجد اختبار جاري.")
        self.quiz_active = False
        if self.scores:
            leaderboard = "\n".join([f"{user}: {points} نقطة" for user, points in self.scores.items()])
            await ctx.send(f"🛑 انتهى الاختبار! النتائج النهائية:\n{leaderboard}")
        else:
            await ctx.send("🛑 انتهى الاختبار! لم يسجل أحد أي نقاط.")
        self.scores.clear()
        self.current_trivia = None

async def setup(bot):
    await bot.add_cog(Quiz(bot))
