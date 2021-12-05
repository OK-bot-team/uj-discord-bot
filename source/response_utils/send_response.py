import discord

from io import BytesIO
from .image_generator import create_image


async def send_response(text, context, author, count):
    print("Message text: " + text[:50])
    with BytesIO() as image_binary:
        create_image(text, author, count).save(image_binary, 'PNG')
        image_binary.seek(0)
        await context.channel.send(file=discord.File(fp=image_binary, filename='image.png'))
