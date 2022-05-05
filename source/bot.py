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
    def __init__(self) -> None:
        self.ready = False
        self.PREFIX = "?"

        super().__init__(
            command_prefix=self.PREFIX, intents=discord.Intents.all()
        )

    def run(self) -> None:
        load_dotenv()

        self.TOKEN = os.getenv("DISCORD_TOKEN")

        if self.TOKEN is None:
            print(
                "Token is not initialized. \
                Be sure to set environmental variable DISCORD_TOKEN",
                flush=True,
            )
            exit(1)

        try:
            super().run(self.TOKEN, reconnect=True)
            print("Bot is active.", flush=True)
        except BaseException as e:
            print(
                f"Unexpected exception while initializing bot: {type(e)}-{e}",
                flush=True,
            )
            exit(2)

    async def on_connect(self) -> None:
        print("OkBot has connected.", flush=True)

    async def on_disconnect(self) -> None:
        print("OkBot has disconnected.", flush=True)

    async def on_ready(self) -> None:
        if not self.ready:
            await self.change_presence(
                activity=discord.Game(name="Type ?background")
            )
            print("Bot ready.", flush=True)
        else:
            print("Bot reconnected", flush=True)

    async def on_error(self, error, *args, **kwargs) -> None:
        if error == "on_command_error":
            await args[0].send("A command error occurred.")
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("Co tam wariacie?")
        elif hasattr(exc, ["original"]):
            raise exc.original
        else:
            raise exc

    async def on_message(self, message: str) -> None:
        if not message.author.bot:
            print(message.content, flush=True)
            await self.process_commands(message)

            if len(message.content) == 0 or message.content[0] == self.PREFIX:
                return

            nickname = message.author.display_name
            response = get_text(message.content, nickname)

            if response["text"] is not None:
                await send_response(response, message, message.author)
                if response["delete"] is True:
                    await message.delete()
            elif randint(1, 4000) >= 3999:
                await send_response(nickname, message, message.author, True)


bot = Bot()


@bot.command()
async def tic(ctx) -> None:
    """Starts a tic-tac-toe game."""
    await ctx.send("Tic Tac Toe: X goes first", view=TicTacToe())


@bot.command()
async def google(ctx, *, query: str) -> None:
    """Returns a google link for a query"""
    await ctx.send(f"Google Result for: `{query}`", view=Google(query))


@bot.command(brief="Set reminder [time] [unit = s,m,h,d,M]")
async def remindme(ctx, amount, unit) -> None:
    await remindme_util(ctx, amount, unit)


@bot.command(
    brief="Get current link to website, \
        where you can change your response background."
)
async def background(ctx) -> None:
    await ctx.send(
        "Change your background on our site:\nhttp://vps-348e48ae.vps.ovh.net/"
    )


def start_bot():
    bot.run()
