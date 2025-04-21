import pytesseract
from PIL import Image

path = '/Users/jack/Desktop/截屏2022-01-26 上午9.12.38.png'
testdata_dir_config = '/Users/jack/Desktop/截屏2022-01-26 上午9.12.38.png'
textCode = pytesseract.image_to_string(Image.open(path), config=testdata_dir_config, lang='eng')

print(textCode)
