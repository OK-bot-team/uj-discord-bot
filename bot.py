import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from image_generator import create_image
from PIL import Image
from io import BytesIO
from random import randint
import re

async def response(text, context):
    print(text)
    with BytesIO() as image_binary:
        create_image(text).save(image_binary, 'PNG')
        image_binary.seek(0)
        await context.channel.send(file=discord.File(fp=image_binary, filename='image.png'))
        

def main():
    client = commands.Bot(command_prefix="?")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected")

    @client.event
    async def on_message(ctx):
        text = re.search(r"(?<=\:[oO][kK]).*(?=\:)", ctx.content)

        if(text):
            await response(text.group(0), ctx)
            await ctx.delete()
        elif (randint(1, 2000) >= 1999 and ctx.author != client.user):
            nickname = str(ctx.author)[0:-5]
            await response(nickname, ctx)

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
