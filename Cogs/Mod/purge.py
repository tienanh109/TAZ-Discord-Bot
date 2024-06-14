print("Loading purge...")
import discord
from discord.ext import commands

class PurgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='purge', description='Delete a specified number of messages')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, number_of_messages: int):
        await ctx.defer()
        deleted = await ctx.channel.purge(limit=number_of_messages)
        await ctx.respond(f'Successfully deleted {len(deleted)} messages.', ephemeral=True)

def setup(bot):
    bot.add_cog(PurgeCog(bot))