import pytesseract
from PIL import Image


url = "/Users/jack/Desktop/DATABASE_statement.png"


def convert_img(path):
    testdata_dir_config = path
    text_code = pytesseract.image_to_string(Image.open(path), config=testdata_dir_config, lang='eng')
    return text_code


# print(convert_img(url))


