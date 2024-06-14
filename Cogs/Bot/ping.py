print("Loading ping...")
import discord
from discord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Ping the bot")
    async def ping(self, ctx):
        latency = self.bot.latency * 1000  # Latency in milliseconds
        await ctx.respond(f"Pong! Latency is {latency:.2f}ms.")

def setup(bot):
    bot.add_cog(PingCog(bot))