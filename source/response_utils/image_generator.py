import os
import re
import requests

from typing import Optional
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from dotenv import load_dotenv


# API url with slash!
load_dotenv()
API_URL = os.getenv("API_URL")

TEXT_FONT = "fonts/Roboto/Roboto-Regular.ttf"
EMOJI_FONT = "fonts/Noto_Emoji/NotoEmoji-Regular.ttf"
IMG_TEXT_MEASURE = Image.new("RGB", (1, 1))
DRAW_TEXT_MEASURE = ImageDraw.Draw(IMG_TEXT_MEASURE)
TEXT_SIZE_LIMIT = 3000


def get_text_dimensions(text: str, font):
    width, height = DRAW_TEXT_MEASURE.textsize(text, font)
    width = TEXT_SIZE_LIMIT if width > TEXT_SIZE_LIMIT else width
    height = TEXT_SIZE_LIMIT if height > TEXT_SIZE_LIMIT else height
    return width, height


def contains_polish_letters(text: str) -> str:
    return re.search(r"[żółćęśąźń]", text) is not None


def create_image(response: dict[str, bool, bool], author: str) -> Image:
    text = response["text"]
    fontsize = 40 if len(text) > 100 else 80

    color = (255, 255, 255)
    font = ImageFont.truetype(
        TEXT_FONT, fontsize, encoding="unic"
    )  # TODO: better font

    text_width, text_height = get_text_dimensions(text, font)

    W = int(text_width * 1.1) + 150
    H = int(text_height * 1.1) + 30
    H = W // 10 if (10 * H < W) else H
    position = ((W - text_width) / 2, (H - text_height) / 2)

    background = get_background(author.id)
    if background is None:
        img = Image.new("RGB", (W, H))
    else:
        img = Image.open(BytesIO(background))
        img = img.resize((W, H))

    draw = ImageDraw.Draw(img)
    draw.text(position, text, color, font=font)

    emoji_font = font = ImageFont.truetype(EMOJI_FONT, 80, encoding="unic")
    draw.text(
        (10, min(int(text_height / 2 - 15), 150)),
        "👌",
        color,
        font=emoji_font,
    )

    return img


def get_background(id: str) -> Optional[bytes]:
    if API_URL == "":
        return

    url = f"{API_URL}api/get-background/{id}"
    try:
        response = requests.get(url, stream=True)
    except requests.ConnectionError:
        print("ERROR: Website does not exist!")
        return

    if response.status_code == 200:
        return response.content
    else:
        print("ERROR: " + str(response.status_code), flush=True)
