import discord
import os

from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv
from random import randint

from .commands.remindme import remindme_util
from .commands.tictactoe import TicTacToe
from .commands.google import Google
from .response_utils.get_text import get_text
from .response_utils.send_response import send_response


class Bot(BotBase):
    def __init__(self):
        self.ready = False
        self.PREFIX = "?"

        super().__init__(
            command_prefix=self.PREFIX
        )

    def run(self):
        load_dotenv()

        self.TOKEN = os.getenv("DISCORD_TOKEN")

        print("Bot is active.")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("OkBot has connected.")

    async def on_disconnect(self):
        print("OkBot has disconnected.")

    async def on_ready(self):
        if not self.ready:
            await self.change_presence(activity=discord.Game(name="Type ?background"))
            print("Bot ready.")
        else:
            print("Bot reconnected")

    async def on_error(self, error, *args, **kwargs):
        if error == "on_command_error":
            await args[0].send("A command error occurred.")
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("Wrong command")
        elif hasattr(exc, ["original"]):
            raise exc.original
        else:
            raise exc

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

            nickname = message.author.display_name
            text, count = get_text(message.content, nickname)

            if text:
                await send_response(text, message, message.author, count)

                if count <= 2:
                    await message.delete()

            elif randint(1, 2000) >= 1999:
                await send_response(nickname, message, message.author, count)


bot = Bot()


def get_bot():
    return bot


@bot.slash_command(guild_ids=[848921520776413213])
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


@bot.command()
async def tic(ctx):
    """Starts a tic-tac-toe game with yourself."""
    await ctx.send("Tic Tac Toe: X goes first", view=TicTacToe())


@bot.command()
async def google(ctx, *, query: str):
    """Returns a google link for a query"""
    await ctx.send(f"Google Result for: `{query}`", view=Google(query))


@bot.command(brief="Set reminder [time] [unit = s,m,h,d,M]")
async def remindme(ctx, amount, unit):
    await remindme_util(ctx, amount, unit)
