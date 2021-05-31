import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from image_generator import create_image

def main():
    client = commands.Bot(command_prefix="?")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected")

    @client.event
    async def on_message(ctx):
        if(ctx.content.startswith(":ok") and ctx.content[-1] == ":"):
            arg = ctx.content[3:-1]
            create_image(arg)
            print(arg)
            p = discord.File("images/response.png")
            await ctx.channel.send(file=p)
            os.remove("images/response.png")

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
