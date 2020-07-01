import pytesseract
from PIL import Image


def convert():
    img = Image.open('images/testimage.png')
    return pytesseract.image_to_string(img)
