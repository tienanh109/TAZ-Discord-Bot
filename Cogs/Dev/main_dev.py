print("Loading maindev... (get_ip, check_port, check_status_code)")
import socket
import time
from discord.ext import commands

class DeveloperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='get_ip', description='Get the IP address of a website')
    async def get_ip(self, ctx, website: str):
        try:
            ip = socket.gethostbyname(website)
            await ctx.respond(f'The IP address of {website} is {ip}')
        except socket.gaierror:
            await ctx.respond(f'Invalid website or unable to resolve IP address.')

    @commands.slash_command(name='check_port', description='Check if a port is open on a website')
    async def check_port(self, ctx, website: str, port: int):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)  # Timeout after 2 seconds
                result = s.connect_ex((website, port))
                if result == 0:
                    await ctx.respond(f'Port {port} is open on {website}')
                else:
                    await ctx.respond(f'Port {port} is not open on {website}')
        except socket.gaierror:
            await ctx.respond(f'Invalid website: {website}')
        except Exception as e:
            await ctx.respond(f'Error checking port: {e}')

    @commands.slash_command(name='check_status_code', description='Check the HTTP status code of a website')
    async def check_status_code(self, ctx, website: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://{website}') as response:
                    status = response.status
                    await ctx.respond(f'Status code for {website}: {status}')
        except aiohttp.ClientConnectorError:
            await ctx.respond(f'Cannot connect to {website}')
        except Exception as e:
            await ctx.respond(f'Error checking status code: {e}')

def setup(bot):
    bot.add_cog(DeveloperCog(bot))