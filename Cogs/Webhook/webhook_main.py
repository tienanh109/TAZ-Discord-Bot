print("Loading create_webhook...")
import discord
from discord.ext import commands

class WebhookCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='create_webhook', description='Create a new webhook')
    @commands.has_permissions(manage_webhooks=True)
    async def create_webhook(self, ctx, channel: discord.TextChannel, name: str):
        try:
            webhook = await channel.create_webhook(name=name)
            await ctx.respond(f'Webhook created successfully: {webhook.url}')
        except discord.Forbidden:
            await ctx.respond('I do not have permission to manage webhooks.')

    @create_webhook.error
    async def webhook_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond('You do not have permission to manage webhooks.')
        elif isinstance(error, commands.BadArgument):
            await ctx.respond('Invalid arguments provided.')

def setup(bot):
    bot.add_cog(WebhookCog(bot))