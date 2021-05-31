import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from image_generator import create_image
from PIL import Image
from io import BytesIO

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
            print(arg)
            with BytesIO() as image_binary:
                create_image(arg).save(image_binary, 'PNG')
                image_binary.seek(0)
                await ctx.channel.send(file=discord.File(fp=image_binary, filename='image.png'))

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
