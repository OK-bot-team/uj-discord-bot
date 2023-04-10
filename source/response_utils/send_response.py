import discord

from io import BytesIO
from .image_generator import create_image


async def send_response(
    response: dict[str, bool], message, author,
) -> None:
    if response["image"]:
        with BytesIO() as image_binary:
            create_image(response, author).save(image_binary, "PNG")
            image_binary.seek(0)
            await message.channel.send(
                file=discord.File(fp=image_binary, filename="image.png")
            )
    else:
        await message.channel.send(response["text"])
