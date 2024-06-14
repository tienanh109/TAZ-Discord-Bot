print("Loading time...")
import discord
from discord.ext import commands
import pytz
from datetime import datetime

class TimeCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="time", description="Show current time in different continents.")
    async def time(self, ctx, continent: str = None):
        if continent is None:
            await ctx.respond("Please specify a continent: /time asia, /time europe, /time africa, /time northamerica, /time southamerica")
        elif continent.lower() == "asia":
            await self.show_time_in_continents(ctx, "Asia", [
                'Asia/Tokyo',       # Japan Standard Time
                'Asia/Seoul',       # Korean Standard Time
                'Asia/Shanghai',    # China Standard Time
                'Asia/Singapore',   # Singapore Time
                'Asia/Kolkata',     # India Standard Time
                'Asia/Bangkok',     # Indochina Time
                'Asia/Dubai',       # Gulf Standard Time
                'Asia/Jakarta'      # Western Indonesia Time
            ], color=0x00ff00)  # Green embed color
        elif continent.lower() == "europe":
            await self.show_time_in_continents(ctx, "Europe", [
                'Europe/London',    # Greenwich Mean Time
                'Europe/Berlin',    # Central European Time
                'Europe/Moscow',    # Moscow Standard Time
                'Europe/Paris',     # Central European Summer Time
                'Europe/Istanbul',  # Turkey Time
                'Europe/Rome',      # Central European Summer Time
                'Europe/Madrid'     # Central European Summer Time
            ], color=0x0000ff)  # Blue embed color
        elif continent.lower() == "africa":
            await self.show_time_in_continents(ctx, "Africa", [
                'Africa/Cairo',     # Eastern European Time
                'Africa/Johannesburg',  # South Africa Standard Time
                'Africa/Lagos',     # West Africa Time
                'Africa/Nairobi',   # East Africa Time
                'Africa/Algiers',   # Central European Time
                'Africa/Casablanca' # Western European Time
            ], color=0xffff00)  # Yellow embed color
        elif continent.lower() == "northamerica":
            await self.show_time_in_continents(ctx, "North America", [
                'America/New_York',  # Eastern Standard Time
                'America/Los_Angeles',  # Pacific Standard Time
                'America/Chicago',   # Central Standard Time
                'America/Denver',    # Mountain Standard Time
                'America/Toronto',   # Eastern Standard Time
                'America/Vancouver', # Pacific Standard Time
                'America/Mexico_City' # Central Standard Time
            ], color=0xff0000)  # Red embed color
        elif continent.lower() == "southamerica":
            await self.show_time_in_continents(ctx, "South America", [
                'America/Buenos_Aires', # Argentina Time
                'America/Sao_Paulo',   # Brasilia Time
                'America/Bogota',       # Colombia Time
                'America/Lima',         # Peru Time
                'America/Caracas',      # Venezuela Time
                'America/Santiago',     # Chile Standard Time
                'America/Guyana'        # Guyana Time
            ], color=0xffa500)  # Orange embed color
        else:
            await ctx.respond("Invalid continent specified. Please use one of: asia, europe, africa, northamerica, southamerica")

    async def show_time_in_continents(self, ctx, continent_name, timezones, color=0x00ff00):
        embed = discord.Embed(title=f"Current Time in Major {continent_name} Timezones", description=f"This bot shows the current time in major {continent_name} timezones.", color=color)

        for tz in timezones:
            current_time = datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S')
            embed.add_field(name=tz, value=current_time, inline=False)
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(TimeCommands(bot))