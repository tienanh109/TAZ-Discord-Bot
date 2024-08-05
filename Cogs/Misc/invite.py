print("Loading invite")
import discord
from discord.ext import commands

class InviteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Get the bot invite link")
    async def invite(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"> You can invite me at: https://discord.com/oauth2/authorize?client_id={self.bot.id}&permissions=1514982992118&scope=bot")

def setup(bot):
    bot.add_cog(InviteCog(bot))