print("Loading weather...")
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
API_KEY = os.getenv("API_WEATHER_KEY")


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name='weather', description='Get weather information for a city.')
    async def weather_info(self, ctx, *, city_name):
        await ctx.defer()
        if not city_name:
            await ctx.respond("Please provide a city name. Example: `!weather Hanoi`")
            return

        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}')
        data = json.loads(response.text)

        if 'error' in data:
            await ctx.respond("Sorry, weather information could not be retrieved.")
            return

        # Extract necessary weather data
        location_name = data['location']['name']
        temperature_c = data['current']['temp_c']
        condition_text = data['current']['condition']['text']
        feelslike_c = data['current']['feelslike_c']
        humidity = data['current']['humidity']
        visibility = data['current']['vis_km']
        wind_kph = data['current']['wind_kph']
        uv = data['current']['uv']
        dewpoint_c = data['current'].get('dewpoint_c', 'Unknown')

        # Create embed for weather information
        embed = discord.Embed(
            title=f"Weather in {location_name}",
            color=discord.Color.blue(),
            description=(
                f"**Temperature:** {temperature_c}°C\n"
                f"**Condition:** {condition_text}\n"
                f"**Feels like:** {feelslike_c}°C\n"
                f"**Humidity:** {humidity}%\n"
                f"**Visibility:** {visibility} km\n"
                f"**Wind:** {wind_kph} kph\n"
                f"**UV Index:** {uv}\n"
                f"**Dewpoint:** {dewpoint_c}°C"
            )
        )
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Weather(bot))