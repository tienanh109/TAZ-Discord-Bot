print("Loading emoji commands... (uploademoji, deleteemoji)")
import discord
from discord.ext import commands

class EmojiCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="uploademoji", description="Upload a custom emoji.")
    async def upload_emoji(self, ctx, name: str, url: str):
        try:
            emoji = await ctx.guild.create_custom_emoji(name=name, image=open(url, 'rb').read())
            await ctx.send(f"Emoji {emoji.name} uploaded successfully: {emoji}")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to upload emoji: {e}")

    @commands.slash_command(name="deleteemoji", description="Delete a custom emoji.")
    async def delete_emoji(self, ctx, emoji: discord.Emoji):
        try:
            await emoji.delete()
            await ctx.send(f"Emoji {emoji.name} deleted successfully.")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to delete emoji: {e}")

def setup(bot):
    bot.add_cog(EmojiCommands(bot))