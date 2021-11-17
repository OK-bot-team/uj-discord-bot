import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from image_generator import create_image
from PIL import Image
from io import BytesIO
from random import randint
import re
import asyncio


async def response(text, context, author, count):
    print("Message text: " + text[:50])
    with BytesIO() as image_binary:
        create_image(text, author, count).save(image_binary, 'PNG')
        image_binary.seek(0)
        await context.channel.send(file=discord.File(fp=image_binary, filename='image.png'))

#returns text, number of escape symbols
# 0- delete original message
# 1- delete original and do not prepend "ok"
# 2- delete original and do not prepend "ok" nor emoji
# 3- do not delete and do not prepend "ok" nor emoji
def get_text(message, author = None):
    regx = re.search(r"(?<=;[oO][kK])(~*)([\s\S]*)(?=;)", message);
    if regx != None:
        return regx.group(2), len(regx.group(1))
    regx = re.search(r"([\s\S]*) [bB]ocie", message);
    if regx != None:
        return regx.group(1) + " " + author, 3
    regx = re.search(r"(kiedy|where) zdalne", message);
    if regx != None:
        return "Nie ma żadnych zdalnych, zdalne wymyśliliście sobie Wy, studenci.", 3
    return None, 0

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
        text, count = get_text(ctx.content, nickname)

        if(text):
            await response(text, ctx, ctx.author, count)
            if count <= 2:
                await ctx.delete()
        elif (randint(1, 2000) >= 1999 and ctx.author != client.user):
            await response(nickname, ctx, ctx.author, count)

    @client.command(brief="Website to change your background")
    async def background(ctx):
        await ctx.send("Change your background on our site:\nhttp://vps-348e48ae.vps.ovh.net/")

    @client.command(brief="Set reminder [time] [unit = s,m,h,d,M]")
    async def remindme(ctx, amount, unit):
        time_offsets = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'M': 2592000}

        if unit not in time_offsets.keys(): 
            await ctx.send("Wrong unit type")
            return
        try:
            amount = int(amount)
            if amount > 0:
                amount = amount * time_offsets[unit]
                await ctx.send("Started reminder")
                await asyncio.sleep(amount)
                await ctx.reply(f"It's time bro {ctx.author.mention}!")
                await ctx.author.send("Its time bro!")
        except:
            await ctx.send("Time must be an integer")
            return

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
