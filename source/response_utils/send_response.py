import discord

from io import BytesIO
from .image_generator import create_image


async def send_response(
    response: dict[str, bool], context, author: str,
) -> None:
    if response["image"]:
        with BytesIO() as image_binary:
            create_image(response, author).save(image_binary, "PNG")
            image_binary.seek(0)
            await context.channel.send(
                file=discord.File(fp=image_binary, filename="image.png")
            )
    else:
        await context.channel.send(response["text"])
