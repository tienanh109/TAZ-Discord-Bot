print("Loading info...")
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time
from psutil import virtual_memory, cpu_count
from psutil._common import bytes2human

load_dotenv()

class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.slash_command(description="Display information about TAZ Bot")
    async def info(self, ctx):
        # Getting the latency
        latency = round(self.bot.latency * 1000, 2)
        
        embed = discord.Embed(
            title="About TAZ Bot",
            color=discord.Color.orange(),
            description=(
                "**General Information:**\n"
                "Name: TAZ Bot\n"
                f"ID: {self.bot.id}\n"
                "Language: English\n"
                f"Servers: {len(self.bot.guilds)}\n\n"
                "**Author Information:**\n"
                "Username: tienanh109\n"
                "[GitHub](https://github.com/tienanh109)\n"
                "[Website](https://tienanh109.dev)\n"
                "[Discord Server](https://tienanh109.dev/dc)\n\n"
                "**Configuration Information:**"
            )
        )
        
        # Setting the bot's avatar as the thumbnail
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.add_field(name="Hosting Service", value="Jenny (with DisCloud)")
        BOT_VERSION = os.getenv('BOT_VERSION')
        embed.add_field(name="Current Version:", value=f"{BOT_VERSION}", inline=False)
        embed.add_field(name="System Information", value=f"{cpu_count()} | {bytes2human(virtual_memory()[0])} RAM", inline=False) # CPU Cores | RAM, there HAS to be a better way to do this, but i just woke up so i'm not thinking at all
        embed.add_field(name="Ping", value=f"{latency} ms", inline=True)
        
        # Footer
        embed.set_footer(text=f"Request by {ctx.author}")
        
        # And... Send!!
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(InfoCog(bot))