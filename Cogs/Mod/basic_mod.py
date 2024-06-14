print("Loading basic (kick, ban, create_channel, give_role, calculate)")
import discord
from discord.ext import commands

class BasicMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Kick users")
    async def kick(self, ctx, user: discord.Member):
        if ctx.author.guild_permissions.kick_members:
            await user.kick()
            await ctx.respond(f"{user.name} has been kicked.")
        else:
            await ctx.respond("You do not have permission to kick users.")

    @commands.slash_command(description="User ban")
    async def ban(self, ctx, user: discord.Member):
        if ctx.author.guild_permissions.ban_members:
            await user.ban()
            await ctx.respond(f"{user.name} has been banned.")
        else:
            await ctx.respond("You do not have permission to ban users.")

    @commands.slash_command(description="Create a new channel")
    async def create_channel(self, ctx, name: str):
        if ctx.author.guild_permissions.manage_channels:
            guild = ctx.guild
            await guild.create_text_channel(name)
            await ctx.respond(f"Channel {name} has been created.")
        else:
            await ctx.respond("You do not have permission to create a channel.")

    @commands.slash_command(description="Assign roles to users")
    async def give_role(self, ctx, user: discord.Member, role: discord.Role):
        if ctx.author.guild_permissions.manage_roles:
            await user.add_roles(role)
            await ctx.respond(f"{user.name} has been assigned the role {role.name}.")
        else:
            await ctx.respond("You do not have permission to assign roles.")

    @commands.slash_command(description="Calculate expressions")
    async def calculate(self, ctx, expression: str):
        try:
            result = eval(expression)
            await ctx.respond(f"Result: {result}")
        except Exception as e:
            await ctx.respond(f"Error: {e}")

def setup(bot):
    bot.add_cog(BasicMod(bot))