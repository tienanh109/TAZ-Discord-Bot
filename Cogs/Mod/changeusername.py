print("Loading changeusername....")
import discord
from discord.ext import commands
from discord import option

class UsernameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='changeusername', description='Change your username')
    @option('new_username', description='New username', required=True)
    async def change_username(self, ctx, new_username: str):
        await ctx.defer()

        try:
            await ctx.author.edit(nick=new_username)
            await ctx.respond(f'Username changed to {new_username}')
        except discord.Forbidden:
            await ctx.respond('I do not have permission to change your username.')

def setup(bot):
    bot.add_cog(UsernameCog(bot))