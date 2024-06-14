print("Loading meme...")
import discord
from discord.ext import commands
import requests
import random

class MemeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='meme', description='Generate a random meme')
    async def meme(self, ctx):
        meme = self.get_random_meme()
        if meme:
            embed = discord.Embed(title=meme['name'])
            embed.set_image(url=meme['url'])
            await ctx.respond(embed=embed, view=MemeView(self.bot))
        else:
            await ctx.respond('Could not fetch a meme at the moment. Please try again later.')

    def get_random_meme(self):
        response = requests.get('https://api.imgflip.com/get_memes')
        if response.status_code == 200:
            data = response.json()
            memes = data['data']['memes']
            return random.choice(memes)
        return None

class MemeView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=60)
        self.bot = bot

    @discord.ui.button(label='Next', style=discord.ButtonStyle.primary)
    async def next_meme(self, button: discord.ui.Button, interaction: discord.Interaction):
        meme = self.get_random_meme()
        if meme:
            embed = discord.Embed(title=meme['name'])
            embed.set_image(url=meme['url'])
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message('Could not fetch a meme at the moment. Please try again later.')

    def get_random_meme(self):
        response = requests.get('https://api.imgflip.com/get_memes')
        if response.status_code == 200:
            data = response.json()
            memes = data['data']['memes']
            return random.choice(memes)
        return None

def setup(bot):
    bot.add_cog(MemeCog(bot))