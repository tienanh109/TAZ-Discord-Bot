print("Loading say...")
import discord
from discord.ext import commands

class FunSayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Send anonymous messages as a bot")
    async def say(self, ctx, message: str):
        if "@everyone" in message or "@here" in message:
            await ctx.respond("You cannot send mentions in your message.", ephemeral=True)
            return
        await ctx.respond("The message has been sent.", ephemeral=True)
        embed = discord.Embed(description=message, color=discord.Color.orange())
        embed.set_author(name="Anonymous", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunSayCog(bot))