# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/29 0029 16:45'


import pytesseract
from PIL import Image

# tesseract路径
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\tesseract\Tesseract-OCR\tesseract.exe"

# 打开图片
image = Image.open(r'D:\Program Files\tesseract\tesseract_imgs\c.png')

# 识别   lang（指定语言）
image_str = pytesseract.image_to_string(image, lang='chi_sim')
print(image_str)
