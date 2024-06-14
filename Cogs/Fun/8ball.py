print("Loading 8ball...")

import discord
from discord.ext import commands
import random
import requests

class EightBallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fallback_responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes, definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

    @commands.slash_command(name="8ball", description="Ask the 8-ball a question!")
    async def eight_ball(self, ctx: discord.ApplicationContext, question: discord.Option(str, description="What is your question?", required=True)):
        await ctx.defer()

        api_url = "https://8ball.delegator.com/magic/JSON/your_question"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            answer = data["magic"]["answer"]
        except (requests.RequestException, KeyError):
            answer = random.choice(self.fallback_responses)

        await ctx.respond(f"🎱 {answer}")

def setup(bot):
    bot.add_cog(EightBallCog(bot))