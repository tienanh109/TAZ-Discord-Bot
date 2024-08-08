print("Loading ping_to_website...")
import aiohttp
import time
from discord.ext import commands

class DeveloperPingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping_to_website', description='Check network latency (ms) to a website')
    async def ping_to_website(self, ctx, website: str):
        try:
            start_time = time.monotonic()
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{website}' if website.startswith("http") else f'https://{website}') as response:
                    latency_ms = (time.monotonic() - start_time) * 1000
                    await ctx.respond(f'Ping to {website} successful. Latency: {latency_ms:.2f} ms')
        except aiohttp.ClientConnectorError:
            await ctx.respond(f'Cannot connect to {website}')
        except Exception as e:
            await ctx.respond(f'Error pinging {website}: {e}')

def setup(bot):
    bot.add_cog(DeveloperPingCog(bot))