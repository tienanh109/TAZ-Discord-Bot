print("Loading help...")
import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Show list of commands")
    async def help(self, ctx):
        commands_list = """
        # TAZ Bot - Help
        ```> Slash Command <
/help - Commands list
/kick <user> - Kick users
/ban <user> - User ban
/create-channel <name> - Create a new channel
/give_role <user> <role> - Assign roles to users
/calculate <expression> - Calculate expressions
/say <message> - Send anonymous messages in the name of bot
/ai-prompt <prompt> - Generate content from prompt 
/google - Google Search
/guess - Guess numbers from 1 to 10 (Random)
/timeout - Timeout 1 user interaction
/userinfo - Show info of user
/ping - Show latency of bot server
/counter <null>
/tic - Play game: Tic Tac Toe (2 Players)
/invite - Receive link to invite TAZ Bot to the server
And more! you can explore using the command / (slash)
Sorry I'm quite lazy :')
```
Bot By **@tienanh109** | Hosted by jenny

        """
        await ctx.respond(commands_list)

def setup(bot):
    bot.add_cog(HelpCog(bot))