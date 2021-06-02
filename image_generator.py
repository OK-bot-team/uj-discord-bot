from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests

# API url with slash!
API_URL = "http://skyman503.pythonanywhere.com/"

def center_text(img, font, text, W, H, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((W-text_width)/2,(H-text_height)/2)
    draw.text(position, text, color, font=font)
    return img


def create_image(text, author):
    W = 1000
    H = 200 * int((1 + text.count('\n') / 3))
    text = "Ok " + str(text)

    background = get_background(author.id)
    if (background == None):
        img = Image.new('RGB', (W, H))
    else:
        img = Image.open(BytesIO(background))
        img = img.resize((W ,H))

    fontsize = 10
    img_fraction = 0.8

    font = ImageFont.truetype("fonts/font.otf", fontsize)
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)

    fontsize = int(min(W / text_width, H / text_height) * 10 * img_fraction)

    font = ImageFont.truetype("fonts/font.otf", fontsize)

    center_text(img, font, str(text), W, H)

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
