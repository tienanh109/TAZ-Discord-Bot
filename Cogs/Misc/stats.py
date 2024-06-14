print("Loading stats... (userinfo, serverinfo)")
import discord
from discord.ext import commands

class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Gets info about a user.")
    async def userinfo(self, ctx: discord.ApplicationContext, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed(
            fields=[
                discord.EmbedField(name="ID", value=str(user.id), inline=False),
                discord.EmbedField(
                    name="Created",
                    value=discord.utils.format_dt(user.created_at, "F"),
                    inline=False,
                ),
            ],
        )
        embed.set_author(name=user.name)
        embed.set_thumbnail(url=user.display_avatar.url)

        if user.colour.value:
            embed.colour = user.colour

        if isinstance(user, discord.User):
            embed.set_footer(text="This user is not in this server.")
        else:
            embed.add_field(
                name="Joined",
                value=discord.utils.format_dt(user.joined_at, "F"),
                inline=False,
            )

        await ctx.respond(embeds=[embed])

    @discord.slash_command(description="Gets info about the server.")
    async def serverinfo(self, ctx: discord.ApplicationContext):
        guild = ctx.guild
        embed = discord.Embed(
            title=guild.name,
            fields=[
                discord.EmbedField(name="Server ID", value=str(guild.id), inline=False),
                discord.EmbedField(name="Owner", value=str(guild.owner), inline=False),
                discord.EmbedField(name="Created", value=discord.utils.format_dt(guild.created_at, "F"), inline=False),
                discord.EmbedField(name="Member Count", value=str(guild.member_count), inline=False),
            ],
            colour=discord.Colour.gold()
        )
        embed.set_thumbnail(url=guild.icon.url)
        await ctx.respond(embeds=[embed])

def setup(bot):
    bot.add_cog(StatsCog(bot))