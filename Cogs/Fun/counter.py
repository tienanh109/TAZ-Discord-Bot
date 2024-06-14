print("Loading counter...")
import discord
from discord.ext import commands

class Counter(discord.ui.View):
    @discord.ui.button(label="0", style=discord.ButtonStyle.red)
    async def count(self, button: discord.ui.Button, interaction: discord.Interaction):
        number = int(button.label) if button.label else 0
        if number >= 9999:
            button.style = discord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)
        await interaction.response.edit_message(view=self)

class CounterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Starts a counter for pressing.")
    async def counter(self, ctx: discord.ApplicationContext):
        await ctx.respond("Press!", view=Counter())

def setup(bot):
    bot.add_cog(CounterCog(bot))