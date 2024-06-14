print("Loading say...")
import discord
from discord.ext import commands

class FunSayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Send anonymous messages as a bot")
    async def say(self, ctx, message: str):
        await ctx.respond("The message has been sent.", ephemeral=True)
        await ctx.send(message)

def setup(bot):
    bot.add_cog(FunSayCog(bot))