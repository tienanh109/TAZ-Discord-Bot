print("Loading createembed...")
import discord
from discord.ext import commands
from discord import option

class EmbedCustomCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='createembed', description='Create a custom embed')
    @option('title', description='Title of the embed', required=True)
    @option('description', description='Description of the embed', required=True)
    @option('footer', description='Footer text of the embed', required=True)
    @option('image', description='URL of the image for the embed')
    @option('thumbnail', description='URL of the thumbnail for the embed')
    @option('incognito', description='Whether to send the embed incognito', type=bool, required=True)
    async def create_embed(self, ctx, title: str, description: str, footer: str, image: str = None, thumbnail: str = None, incognito: bool = False):
        await ctx.defer()
        
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Color.blurple()
        )
        embed.set_footer(text=footer)
        
        if image:
            embed.set_image(url=image)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        
        if incognito:
            # Send the embed to the user only they can see
            await ctx.respond('Sent!', ephemeral=True)
            await ctx.author.send(embed=embed)
        else:
            # Respond with the embed directly in the channel
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(EmbedCustomCog(bot))