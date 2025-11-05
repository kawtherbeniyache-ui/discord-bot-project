import random
from discord.ext import commands

# ======== Riddles ========
RIDDLES = [
    ('ما هو الشيء الذي كلما زاد نقص؟', 'العمر'),
    ('له أوراق وليس شجرة، ما هو؟', 'الكتاب'),
    ('ما الشيء الذي يكتب ولا يقرأ؟', 'القلم'),
]

# ======== Trivia Questions ========
TRIVIA_QUESTIONS = [
    {
        "question": "عاصمة فرنسا؟",
        "options": ["A) باريس", "B) لندن", "C) روما", "D) برلين"],
        "answer": "A"
    },
    {
        "question": "كم عدد كواكب النظام الشمسي؟",
        "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
        "answer": "B"
    },
]

# ======== Flags Game ========
FLAGS = {
    "🇸🇹": "أفريقيا",
    "🇹🇨": "تركيا",
    "🇸🇰": "سلوفاكيا",
    "🇸🇲": "سان مارينو",
    "🇯🇵": "اليابان",
    "🇧🇷": "البرازيل",
    "🇺🇸": "الولايات المتحدة"
}

# ======== Number Guess ========
class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_trivia = None
        self.current_flag = None
        self.current_number = None

    # ===== Coin Flip =====
    @commands.command(name='coin')
    async def coinflip(self, ctx):
        result = random.choice(['Heads', 'Tails'])
        await ctx.send(f'🪙 النتيجة: **{result}**')

    # ===== Rock Paper Scissors =====
    @commands.command(name='rps')
    async def rock_paper_scissors(self, ctx, choice: str):
        choice = choice.lower()
        options = ['rock','paper','scissors']
        if choice not in options:
            return await ctx.send('استخدم: !rps rock|paper|scissors')
        bot_choice = random.choice(options)
        if choice == bot_choice:
            outcome = 'تعادل'
        elif (choice == 'rock' and bot_choice == 'scissors') or \
             (choice == 'paper' and bot_choice == 'rock') or \
             (choice == 'scissors' and bot_choice == 'paper'):
            outcome = 'فزت'
        else:
            outcome = 'خسرت'
        await ctx.send(f'أنت: **{choice}** — البوت: **{bot_choice}** → **{outcome}**')

    # ===== Riddles =====
    @commands.command(name='riddle')
    async def riddle(self, ctx):
        q,a = random.choice(RIDDLES)
        await ctx.send(f'فزورة: **{q}**\nاكتب !answer <جوابك>')

    # ===== Trivia Quiz =====
    @commands.command(name="quiz")
    async def quiz(self, ctx):
        self.current_trivia = random.choice(TRIVIA_QUESTIONS)
        options_text = "\n".join(self.current_trivia["options"])
        await ctx.send(f"سؤال: {self.current_trivia['question']}\n{options_text}\nاكتب !answer <حرف>")

    # ===== Flags Game =====
    @commands.command(name='flags')
    async def flags_game(self, ctx):
        self.current_flag, country = random.choice(list(FLAGS.items()))
        await ctx.send(f"ما اسم الدولة لهذا العلم؟ {self.current_flag}\nاكتب !answer <اسم الدولة>")

    # ===== Number Guess =====
    @commands.command(name='numberguess')
    async def number_guess(self, ctx):
        self.current_number = random.randint(1,20)
        await ctx.send("خمن رقم بين 1 و 20! اكتب !answer <رقم>")

    # ===== Mafia (Placeholder) =====
    @commands.command(name='mafia')
    async def mafia(self, ctx):
        await ctx.send("لعبة المافيا جاهزة! لكن تحتاج لاعبين لتطوير اللعبة أكثر.")

    # ===== Answer Command =====
    @commands.command(name='answer')
    async def answer(self, ctx, *, guess: str):
        # Riddles
        for _, ans in RIDDLES:
            if ans.lower() in guess.lower():
                return await ctx.send('✅ صح! أحسنت.')

        # Trivia
        if self.current_trivia:
            if guess.upper() == self.current_trivia["answer"]:
                await ctx.send("✅ صح! أحسنت.")
            else:
                await ctx.send(f"❌ خاطئ! الإجابة الصحيحة: {self.current_trivia['answer']}")
            self.current_trivia = None
            return

        # Flags
        if self.current_flag:
            if guess.lower() == FLAGS[self.current_flag].lower():
                await ctx.send("✅ صح! أحسنت.")
            else:
                await ctx.send(f"❌ خاطئ! الإجابة الصحيحة: {FLAGS[self.current_flag]}")
            self.current_flag = None
            return

        # Number Guess
        if self.current_number:
            if guess.isdigit() and int(guess) == self.current_number:
                await ctx.send("✅ صح! أحسنت.")
            else:
                await ctx.send(f"❌ خاطئ! الرقم الصحيح كان: {self.current_number}")
            self.current_number = None
            return

        await ctx.send("❌ لا يوجد سؤال نشط أو الجواب خاطئ.")

# ===== Setup Cog =====
async def setup(bot):
    await bot.add_cog(Games(bot))