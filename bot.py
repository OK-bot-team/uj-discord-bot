import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from image_generator import create_image
from PIL import Image
from io import BytesIO
from random import randint
import re


async def response(text, context, author, raw):
    print("Message text: " + text[:50])
    with BytesIO() as image_binary:
        create_image(text, author, raw).save(image_binary, 'PNG')
        image_binary.seek(0)
        await context.channel.send(file=discord.File(fp=image_binary, filename='image.png'))

def get_text(message, author = None):
    regx = re.search(r"(?<=;[oO][kK])([\s\S]*)(?=;)", message);
    if regx != None:
        return regx.group(0), False
    regx = re.search(r"([\s\S]*) [bB]ocie", message);
    if regx != None:
        return regx.group(1) + " " + author, True
    return None, False

def main():
    client = commands.Bot(command_prefix="?")

    load_dotenv()

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Game(name="Type ?background"))
        print(f"{client.user.name} has connected")

    @client.event
    async def on_message(ctx):
        await client.process_commands(ctx)

        nickname = str(ctx.author)[0:-5]
        text, raw = get_text(ctx.content, nickname)

        if(text):
            await response(text, ctx, ctx.author, raw)
            if not raw:
                await ctx.delete()
        elif (randint(1, 2000) >= 1999 and ctx.author != client.user):
            await response(nickname, ctx, ctx.author, raw)

    @client.command(brief="Website to change your background")
    async def background(ctx):
        await ctx.send("Change your background on our site:\nhttp://vps-348e48ae.vps.ovh.net/")

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
