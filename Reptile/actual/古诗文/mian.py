# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/18 0018 13:43'

import requests
import re


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

    }

    response = requests.get(url=url, headers=headers)
    text = response.text
    return text


def parse_page(html):
    re_title = re.compile("""<div\sclass="cont">  # 获取包含标题的父盒子
                    .*?  # 非贪婪  一遇到第一个<b>就停止；否则 一直贪婪到最后一个cont的<b>
                    <b>(.*?)</b>  # 只匹配()的值；必须非贪婪，否则 贪婪最后一个cont的</b>前的所有数据
    """,re.X)  # re.X  正则字符可以注释

    # 标题
    titles = re.findall('<div\sclass="cont">.*?<b>(.*?)</b>', html, re.DOTALL)  # 默认"."是不匹配空白字符的，re.DOTALL 使其能匹配空白字符
    # print(titles)

    # 朝代
    dynastys = re.findall('<p\sclass="source">.*?target="_blank">(.*?)</a><span>(.*?)</span>.*? target="_blank">(.*?)</a></p>',html, re.DOTALL)

    # print(dynastys)
    contsons = re.findall('<div class="contson" .*?>(.*?)</div>', html, re.DOTALL)
    print(contsons)


def main():
    url = "https://www.gushiwen.org/default_1.aspx"
    html = get_url(url)
    parse_page(html)


if __name__ == '__main__':
    main()

