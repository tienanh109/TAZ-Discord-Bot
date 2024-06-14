print("Loading ai-prompt...")
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_GEMINI_KEY")

class AIPromptCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="ai-prompt", description="Using Gemini API by Google! (Beta)")
    async def ai(self, ctx: discord.ApplicationContext, prompt: str):
        await ctx.respond("🤔 Thinking...")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
        headers = {'Content-Type': 'application/json'}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            content = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            await ctx.edit(content=content)
        else:
            await ctx.respond(content="Error!")

def setup(bot):
    bot.add_cog(AIPromptCog(bot))