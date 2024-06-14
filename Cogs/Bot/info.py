print("Loading info...")
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time

load_dotenv()

class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.slash_command(description="Display information about TAZ Bot")
    async def info(self, ctx):
        # Tính ping
        latency = round(self.bot.latency * 1000, 2)
        
        # Lấy thông tin RAM và dung lượng ổ cứng
        # Tạo embed để hiển thị thông tin
        embed = discord.Embed(
            title="About TAZ Bot",
            color=discord.Color.orange(),
            description=(
                "**General Information:**\n"
                "Name: TAZ Bot\n"
                "ID: 926795496469704765\n"
                "Language: English\n"
                f"Servers: {len(self.bot.guilds)}\n\n"
                "**Author Information:**\n"
                "Username: tienanh109\n"
                "[GitHub](https://github.com/tienanh109)\n"
                "[Website](https://tienanh109.dev)\n"
                "[Discord Server](https://tienanh109.dev/dc)\n\n"
                "**Configuration Information:**"
            )
        )
        
        # Thêm thumbnail là avatar của bot
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.add_field(name="Hosting Service", value="Jenny (with DisCloud)")
        SYSTEM_INFO = os.getenv('SYSTEM_INFO')
        embed.add_field(name="System", value=f"{SYSTEM_INFO}", inline=False)
        embed.add_field(name="Ping", value=f"{latency} ms", inline=True)
        
        # Thêm footer
        embed.set_footer(text=f"Request by {ctx.author}")
        
        # Gửi embed
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(InfoCog(bot))