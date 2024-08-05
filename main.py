import discord
import requests
import datetime
import random
from dotenv import load_dotenv
import os
from discord import Option
from asyncio import TimeoutError
from typing import List
from discord.ext import commands
from urllib.parse import quote_plus

load_dotenv()

TOKEN = os.getenv('MAIN_DISCORD_TOKEN')
STATUS = os.getenv('STATUS')
PREFIX = os.getenv('DISCORD_PREFIX')
BOT_NAME = os.getenv('BOT_NAME')


os.system("cls" if os.name == "nt" else "clear")
print(f"{BOT_NAME} is preparing to run...\n")

intents = discord.Intents.default()


# Initializing the bot variable with prefix and intents
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

for folder in os.listdir('Cogs'):
    folder_path = os.path.join('Cogs', folder)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.py') and not filename.startswith('__'):
                cog_path = f'Cogs.{folder}.{filename[:-3]}'
                try:
                    bot.load_extension(cog_path)
                except Exception as e:
                    print(f'Failed to load cog {cog_path}: {e}')
                    
@bot.event
async def on_ready():
    print(f"\n\n")
    print(f"{BOT_NAME} IS RUNNING NOW!")
    print(f"Info:\nName: {BOT_NAME}\nStatus: {STATUS}\nPrefix: {PREFIX}\n\n({bot.id})\nError Log will show below!!")
    guild_count = len(bot.guilds)
    await bot.change_presence(activity=discord.Game(name=f"{STATUS}"))
        
        
bot.run(TOKEN)