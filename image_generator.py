from PIL import Image, ImageDraw, ImageFont

def center_text(img, font, text, color=(255, 255, 255)):
    W = 700
    H = 200
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((W-text_width)/2,(H-text_height)/2)
    draw.text(position, text, color, font=font)
    return img


def create_image(text):
    W = 700
    H = 200

    text = "Ok " + str(text)

    img = Image.new('RGB', (W, H))
    ok_emoji = Image.open("images/ok.png")

    font = ImageFont.truetype("fonts/font.ttf", 60)
    center_text(img, font, str(text))

    img.paste(ok_emoji, (10, 75))
    return img

