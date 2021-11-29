import os
import re
import requests

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from dotenv import load_dotenv


# API url with slash!
load_dotenv()
API_URL = os.getenv("API_URL")

polish_font = "fonts/font.otf"
emoji_font = "fonts/Symbola.ttf"
ok_emoji = Image.open("images/ok.png")
img_text_measure = Image.new('RGB', (1, 1))
draw_text_measure = ImageDraw.Draw(img_text_measure)


def get_text_dimensions(text, font):
    return draw_text_measure.textsize(text, font)


def create_image(text, author, count):
    fontsize = 80
    if (len(text) > 100):
        fontsize = 40

    if text[:5] == 'black':
        text = text[5:]
        black_background = True
    elif API_URL is None:
        black_background = True
    else:
        black_background = False

    if count == 0:
        text = "Ok " + str(text)

    if re.search(r'[żółćęśąźń]', text) is None:
        emoji = True
        font_path = emoji_font
        if count <= 1:
            text = "👌 " + str(text)
    else:
        emoji = False
        font_path = polish_font

    color = (255, 255, 255)
    font = ImageFont.truetype(
        font_path,
        fontsize,
        encoding='unic')  # TODO: better font

    text_width, text_height = get_text_dimensions(text, font)
    if text_width > 3000:
        text_width = 3000
    if text_height > 3000:
        text_height = 3000

    W = int(text_width * 1.1) + 150
    H = int(text_height * 1.1) + 30
    if (H * 10 < W):
        H = int(W / 10)

    print(text_width, text_height)
    print("Image size: ", W, H,)
    position = ((W - text_width) / 2, (H - text_height) / 2)

    background = None
    if(not black_background):
        background = get_background(author.id)

    if (background is None):
        img = Image.new('RGB', (W, H))
    else:
        img = Image.open(BytesIO(background))
        img = img.resize((W, H))

    draw = ImageDraw.Draw(img)
    draw.text(position, text, color, font=font)

    if not emoji and count <= 1:
        img.paste(ok_emoji, (10, min(int(text_height / 2 - 15), 150)))
    return img


def get_background(id):
    url = f'{API_URL}api/get-background/{id}'
    try:
        response = requests.get(url, stream=True)
    except requests.ConnectionError:
        print("ERROR: Website does not exist!")
        return

    if response.status_code == 200:
        return response.content
    else:
        print("ERROR: " + str(response.status_code))
        return
