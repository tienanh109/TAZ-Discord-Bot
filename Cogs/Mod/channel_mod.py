print("Loading Channel Mod (createcategory, removecategory, createrole, deleterole, createvoicechannel, deletevoicechannel)")
import discord
from discord.ext import commands
from discord import option

class ChannelModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='createcategory', description='Create a new category')
    @option("name", description="Name of the new category", required=True)
    async def create_category(self, ctx, name: str):
        await ctx.defer()
        guild = ctx.guild
        existing_category = discord.utils.get(guild.categories, name=name)
        if existing_category:
            await ctx.respond(f'Category "{name}" already exists.')
        else:
            await guild.create_category(name)
            await ctx.respond(f'Category "{name}" created successfully.')

    @commands.slash_command(name='removecategory', description='Remove a category')
    @option("name", description="Name of the category to remove", required=True)
    async def remove_category(self, ctx, name: str):
        await ctx.defer()
        guild = ctx.guild
        category = discord.utils.get(guild.categories, name=name)
        if category:
            await category.delete()
            await ctx.respond(f'Category "{name}" removed successfully.')
        else:
            await ctx.respond(f'Category "{name}" not found.')

    @commands.slash_command(name='createrole', description='Create a new role')
    @option("name", description="Name of the new role", required=True)
    async def create_role(self, ctx, name: str):
        await ctx.defer()
        guild = ctx.guild
        existing_role = discord.utils.get(guild.roles, name=name)
        if existing_role:
            await ctx.respond(f'Role "{name}" already exists.')
        else:
            await guild.create_role(name=name)
            await ctx.respond(f'Role "{name}" created successfully.')

    @commands.slash_command(name='deleterole', description='Delete a role')
    @option("name", description="Name of the role to delete", required=True)
    async def delete_role(self, ctx, name: str):
        await ctx.defer()
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name=name)
        if role:
            await role.delete()
            await ctx.respond(f'Role "{name}" deleted successfully.')
        else:
            await ctx.respond(f'Role "{name}" not found.')

    @commands.slash_command(name='createvoicechannel', description='Create a new voice channel')
    @option("name", description="Name of the new voice channel", required=True)
    async def create_voice_channel(self, ctx, name: str):
        await ctx.defer()
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.voice_channels, name=name)
        if existing_channel:
            await ctx.respond(f'Voice channel "{name}" already exists.')
        else:
            await guild.create_voice_channel(name)
            await ctx.respond(f'Voice channel "{name}" created successfully.')

    @commands.slash_command(name='deletevoicechannel', description='Delete a voice channel')
    @option("name", description="Name of the voice channel to delete", required=True)
    async def delete_voice_channel(self, ctx, name: str):
        await ctx.defer()
        guild = ctx.guild
        channel = discord.utils.get(guild.voice_channels, name=name)
        if channel:
            await channel.delete()
            await ctx.respond(f'Voice channel "{name}" deleted successfully.')
        else:
            await ctx.respond(f'Voice channel "{name}" not found.')

def setup(bot):
    bot.add_cog(ChannelModCog(bot))