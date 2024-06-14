print("Loading wiki... (wikisearch, summary, wikiurl, wikirandom)")
import discord
from discord.ext import commands
from discord.commands import Option
import wikipedia

class WikiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='wikisearch', description="Search Wikipedia")
    async def wikisearch(self, ctx: discord.ApplicationContext, search: Option(str, description="What do you want to search for?", required=True)):
        await ctx.channel.trigger_typing()  # shows that the bot is typing 
        searchsearch = str(wikipedia.search(search, suggestion=True)).replace('(', '').replace(')', '').replace("'", "").replace('[', '').replace(']', '')  # usually returns a list, so we turn it into a string, suggestion = true includes suggestions
        try:
            await ctx.respond(searchsearch)
        except:
            await ctx.respond(searchsearch)

    @commands.slash_command(name='summary', description='Returns a Wikipedia summary')
    async def summary(self, ctx: discord.ApplicationContext, search: Option(str, description="What do you want to get a summary for?", required=True)):
        await ctx.channel.trigger_typing()  # shows that the bot is typing 
        await ctx.defer()
        try:  # tries to get a summary
            thesummary = wikipedia.summary(search, chars=1950)  # limits the summary to a maximum of 1950 characters, discord's limit is 2,000 per message 
            try:
                await ctx.respond(thesummary)  # responds to the slash command (bot must respond within 3 seconds)
            except:
                await ctx.respond(thesummary)  # sends as a regular message, if it cannot send as a slash command 
        except:
            searchsummary = str(wikipedia.search(search, suggestion=True)).replace('(', '').replace(')', '').replace("'", "").replace('[', '').replace(']', '')  # usually returns a list, so we turn it into a string, suggestion = true includes suggestions
            try:
                await ctx.respond(f"I can't seem to find a summary for that.. Did you mean: {searchsummary}")
            except:
                await ctx.respond(f"I can't seem to find a summary for that.. Did you mean: {searchsummary}")

    @commands.slash_command(name="wikiurl", description="Get a URL to a page on Wikipedia")
    async def wikiurl(self, ctx: discord.ApplicationContext, search: Option(str, description="What do you want to get a URL for?", required=True)):
        await ctx.channel.trigger_typing()
        await ctx.defer()
        try:  # tries to get a summary to see if we can get a link 
            urlsummary = wikipedia.summary(search, auto_suggest=False)  # I think auto suggest is on by default
            search = search.lower().replace(' ', '_').replace('  ', '_')
            try:
                await ctx.respond(f'https://en.wikipedia.org/wiki/{search}')
            except:
                await ctx.respond(f'https://en.wikipedia.org/wiki/{search}')
        except:
            urlsearch = str(wikipedia.search(search, suggestion=True)).replace('(', '').replace(')', '').replace("'", "").replace('[', '').replace(']', '') 
            try:
                await ctx.respond(f"I can't find what you're talking about, did you mean: {urlsearch}")
            except:
                await ctx.respond(f"I can't find what you're talking about, did you mean: {urlsearch}")

    @commands.slash_command(name="wikirandom", description="Returns a random Wikipedia article")
    async def wikirandom(self, ctx: discord.ApplicationContext):
        await ctx.channel.trigger_typing()
        await ctx.defer()
        randomtitle = wikipedia.random()  # returns a title 
        randomsummary = wikipedia.summary(randomtitle, chars=1950)
        link = randomtitle.replace(' ', '_')
        try:
            await ctx.respond(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")
        except:
            await ctx.respond(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")

def setup(bot):
    bot.add_cog(WikiCog(bot))