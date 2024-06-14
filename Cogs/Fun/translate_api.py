print("Loading translate")
import discord
from discord.ext import commands
import aiohttp

class TranslateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='translate', description='Translate text to English')
    async def translate(self, ctx, text: str, target_language: str = 'en'):
        await ctx.defer()
        translation = await self.get_translation(text, target_language)
        if translation:
            content = translation
            await ctx.respond(f"Translated: **{content}**")
        else:
            await ctx.respond('Could not translate the text at the moment. Please try again later.')

    async def get_translation(self, text, target_language):
        async with aiohttp.ClientSession() as session:
            url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_language}&dt=t&q={text}'
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data[0][0][0]
                return None

def setup(bot):
    bot.add_cog(TranslateCog(bot))