print("Loading google...")
import discord
from discord.ext import commands
from urllib.parse import quote_plus

class Google(discord.ui.View):
    def __init__(self, query: str):
        super().__init__()
        query = quote_plus(query)
        url = f"https://www.google.com/search?q={query}"
        self.add_item(discord.ui.Button(label="Click Here", url=url))

class GoogleQueryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Returns a Google link for a query.")
    async def google(self, ctx: discord.ApplicationContext, query: str):
        await ctx.respond(f"Google Result for: `{query}`", view=Google(query))

def setup(bot):
    bot.add_cog(GoogleQueryCog(bot))