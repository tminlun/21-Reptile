# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/29 0029 17:27'


import pytesseract
import time

from urllib import request
from PIL import Image


def main():
    # tesseract路径
    pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\tesseract\Tesseract-OCR\tesseract.exe"
    # 验证码url，url固定，内容动态
    url = r"https://www.kanshu.com/new/login/vdimgck?rnd=0.012661831519990008"

    while True:
        # 不能百分之百识别成功（一直循环到识别成功）

        # 下载图片
        request.urlretrieve(url, "captcha.png")

        # 打开图片
        image = Image.open(r"captcha.png")


        # 识别图片
        text = pytesseract.image_to_string(image)
        print(text)  # text发送到“注册”参数进行验证，验证成功，退出循环

        # 睡眠，防止封ip
        time.sleep(2)


if __name__ == '__main__':
    main()
