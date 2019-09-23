# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/19 0019 14:40'

import requests
import re


comment_url = "http://api.budejie.com/api/api_open.php?a=datalist&per=5&c=comment&hot=0&appname=www&client=www&device=pc&data_id={}&page=3&callback=jQuery180006352018932693881_1568879500497&_=1568879571702"


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        print("获取失败")
        return False
    text = response.text
    return text


# 获取详情url
def datail_urls(html):
    urls = []
    re_urls = re.findall(r'<div class="j-r-list-c-img">\s+<a href="(.*?)".*?', html, re.S)

    for url in re_urls:
        url = 'http://www.budejie.com' + url
        urls.append(url)
    return urls


# 解析详情url的数据
def parse_detail(url):


    print(url)


def main():
    # 获取首页url
    url = "http://www.budejie.com/1"
    html = get_url(url)

    # 获取详情url
    detail_urls = datail_urls(html)
    for detail_url in detail_urls:
        # 解析详情url的数据
        url = get_url(detail_url)
        parse_detail(url)

        break



if __name__ == '__main__':
    main()

