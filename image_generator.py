from PIL import Image, ImageDraw, ImageFont

def center_text(img, font, text, color=(255, 255, 255)):
    W = 1000
    H = 200
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((W-text_width)/2,(H-text_height)/2)
    draw.text(position, text, color, font=font)
    return img


def create_image(text):
    W = 1000
    H = 200

    text = "Ok " + str(text)
    text = ' '.join(text.split())

    img = Image.new('RGB', (W, H))
    ok_emoji = Image.open("images/ok.png")

    fontsize = 1
    img_fraction = 0.8

    font = ImageFont.truetype("fonts/font.otf", fontsize)
    while font.getsize(text)[0] < img_fraction*img.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("fonts/font.otf", fontsize)

    fontsize = min(60, fontsize)
    font = ImageFont.truetype("fonts/font.otf", fontsize)

    center_text(img, font, str(text))

    img.paste(ok_emoji, (10, 75))
    return img

