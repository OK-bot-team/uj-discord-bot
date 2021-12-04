import discord
import os

from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv
from random import randint

from .utils.get_text import get_text
from .utils.send_response import send_response


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


if __name__ == "__main__":
    bot = Bot()
    bot.run()
