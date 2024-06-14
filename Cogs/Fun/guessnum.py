print("Loading guess...")
import discord
import random
from discord.ext import commands
from asyncio import TimeoutError

class GuessNumberCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="guess", description="Guess a number between 1 and 10!")
    async def guess_number(self, ctx: discord.ApplicationContext):
        await ctx.respond("Type in your number. *(It should be between 1 and 10)*")

        def is_valid_guess(m: discord.Message):
            return (
                m.author == ctx.author and m.content.isdigit() and 1 <= int(m.content) <= 10
            )

        answer = random.randint(1, 10)

        try:
            guess: discord.Message = await self.bot.wait_for(
                "message", check=is_valid_guess, timeout=5.0
            )
        except TimeoutError:
            return await ctx.send_followup(f"Sorry, you took too long it was {answer}.")

        if int(guess.content) == answer:
            await guess.reply("You are right!", mention_author=True)
        else:
            await guess.reply(f"Oops. It is actually {answer}.", mention_author=True)

def setup(bot):
    bot.add_cog(GuessNumberCog(bot))