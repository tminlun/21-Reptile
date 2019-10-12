# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/9 0009 15:58'


import requests
import os
import re
import time

from lxml import etree
from urllib import request


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': 'http://www.doutula.com/photo/list/?page=1'
    }
    response = request.Request(url,headers=headers)
    text = request.urlopen(response)

    html = text.read().decode('utf-8')
    parse_page(html)


def parse_page(text):
    html = etree.HTML(text)
    imgs = html.xpath('//div[contains(@class, "page-content")]//img[@class!="gif"]')
    for img in imgs:

        # get()  获取元素的属性
        img_url = img.get('data-original')  # 图片url
        img_name = str(img.get('alt'))  # 图片名 + 后缀

        # 后缀名
        img_name = re.sub(r'[\.。\?？!！,，]', '', img_name)  # 替换
        suffix = os.path.splitext(img_url)[-1]

        # 重命名
        filename = img_name + suffix

        # 下载图片
        dir = os.path.abspath('images/')
        work_path = os.path.join(dir, filename)

        try:
            request.urlretrieve(img_url, work_path)  # 文件，文件名（异常：urllib.error.HTTPError: HTTP Error 403: Forbidden）
        except Exception:
            continue


def main():
    for x in range(1, 4):
        print(f'爬取斗图王，第{x}页')
        url = f'http://www.doutula.com/photo/list/?page={x}'
        get_url(url)

        time.sleep(1)


if __name__ == '__main__':
    main()

