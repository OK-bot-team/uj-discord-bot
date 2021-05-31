from PIL import Image, ImageDraw, ImageFont

def create_image(text):
    img = Image.new('RGB', (500, 500), color = (73, 109, 137))

    d = ImageDraw.Draw(img)
    d.text((200,10), str(text), fill=(255, 255, 0))

    img.save('images/response.png')