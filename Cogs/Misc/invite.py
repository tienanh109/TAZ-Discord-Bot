print("Loading invite")
import discord
from discord.ext import commands

class InviteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Get the bot invite link")
    async def invite(self, ctx: discord.ApplicationContext):
        await ctx.respond("> You can invite me at: https://discord.com/oauth2/authorize?client_id=926795496469704765&permissions=8&scope=bot")

def setup(bot):
    bot.add_cog(InviteCog(bot))