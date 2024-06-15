print("Loading vote...")
import discord
from discord.ext import commands

class VoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Vote for TAZ Bot")
    async def vote(self, ctx):
        commands_list = "> You can vote for us at: \n> https://discord.com/oauth2/authorize?client_id=926795496469704765&permissions=8&scope=bot \n> ***Thank you so much 💖!***"
        await ctx.respond(commands_list)

def setup(bot):
    bot.add_cog(VoteCog(bot))
