print("Loading restart...")
import discord
import os
import asyncio
import sys
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
OWNER = int(os.getenv("OWNER_USERNAME"))

def setup(bot):
    @bot.command()
    async def restart(ctx):
      if ctx.author.id == OWNER:
          await ctx.reply("Will do it as soon as possible!")
          await asyncio.sleep(1)
          python = sys.executable
          os.execl(python, python, *sys.argv)
      else:
        await ctx.reply("You do not have permission to execute this command!")