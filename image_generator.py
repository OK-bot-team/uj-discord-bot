from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests

# API url with slash!
API_URL = "http://skyman503.pythonanywhere.com/"


def get_text_dimensions(text, font):
    img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(img)
    return draw.textsize(text, font)


def create_image(text, author):
    fontsize = 90
    if (len(text) > 100):
        fontsize = 45
    color = (255, 255, 255)
    font = ImageFont.truetype("fonts/font.otf", fontsize)
    text = "Ok " + str(text)

    text_width, text_height = get_text_dimensions(text, font)
    W = max(1000, int(text_width * 1.1) + 30)
    H = max(200, int(text_height * 1.1) + 30)
    print(text_width, text_height)
    print("Image size: ", W, H,)
    position = ((W - text_width) / 2, (H - text_height) / 2)

    background = get_background(author.id)
    if (background is None):
        img = Image.new('RGB', (W, H))
    else:
        img = Image.open(BytesIO(background))
        img = img.resize((W, H))

    draw = ImageDraw.Draw(img)
    draw.text(position, text, color, font=font)

    ok_emoji = Image.open("images/ok.png")
    img.paste(ok_emoji, (10, 75))
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
