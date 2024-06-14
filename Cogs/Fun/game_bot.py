print("Loading GameBot...  (joke, fact, rps)")
import discord
from discord.ext import commands
import aiohttp
import random

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='joke', description='Send a random joke in English')
    async def joke(self, ctx):
        joke = await self.get_joke()
        if joke:
            await ctx.respond(joke)
        else:
            await ctx.respond('Could not fetch a joke at the moment. Please try again later.')

    async def get_joke(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://official-joke-api.appspot.com/jokes/random') as response:
                if response.status == 200:
                    data = await response.json()
                    return f"{data['setup']} - {data['punchline']}"
                return None

    @commands.slash_command(name='fact', description='Send a random fact')
    async def fact(self, ctx):
        fact = await self.get_fact()
        if fact:
            await ctx.respond(fact)
        else:
            await ctx.respond('Could not fetch a fact at the moment. Please try again later.')

    async def get_fact(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://uselessfacts.jsph.pl/random.json?language=en') as response:
                if response.status == 200:
                    data = await response.json()
                    return data['text']
                return None


    @commands.slash_command(name='rps', description='Play rock-paper-scissors with the bot')
    async def rps(self, ctx, choice: str):
        choices = ['rock', 'paper', 'scissors']
        if choice not in choices:
            await ctx.respond('Please choose rock, paper, or scissors.')
            return

        bot_choice = random.choice(choices)
        result = self.determine_rps_winner(choice, bot_choice)
        await ctx.respond(f'You chose {choice}, I chose {bot_choice}. {result}')

    def determine_rps_winner(self, user_choice, bot_choice):
        if user_choice == bot_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and bot_choice == 'scissors') or \
             (user_choice == 'scissors' and bot_choice == 'paper') or \
             (user_choice == 'paper' and bot_choice == 'rock'):
            return 'You win!'
        else:
            return 'I win!'

def setup(bot):
    bot.add_cog(FunCog(bot))