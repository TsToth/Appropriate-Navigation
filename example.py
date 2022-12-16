import os

from webex_bot.commands.echo import EchoCommand
from webex_bot.webex_bot import WebexBot

# Create a Bot Object
bot = WebexBot(teams_bot_token=os.getenv("NjVjYjJmYzUtYzFkNi00ZmRkLWIzMmYtNTgxMzAyZDljODk5NjZjN2U1YzAtMmRk_P0A1_ff79c397"),
               approved_rooms=[''],
               bot_name="bot1",
               include_demo_commands=True)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())

# Call `run` for the bot to wait for incoming messages.
bot.run()