print("Loading slow mode...")
import discord
from discord.ext import commands

class SlowmodeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='slowmode', description='Set slow mode in a channel')
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        try:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.respond(f'Set slow mode delay to {seconds} seconds in {ctx.channel.mention}')
        except discord.Forbidden:
            await ctx.respond('I do not have permission to manage channels.')

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond('You do not have permission to manage channels.')

def setup(bot):
    bot.add_cog(SlowmodeCog(bot))