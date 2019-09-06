# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/6 0006 13:10'

import requests
from lxml import etree

'''
爬取豆瓣电影的正在热映：xpath和requests
'''

# 1.爬取网页数据
def get_url():
    headers = {
        # 浏览器名称
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        # 根据Referer判断请求是否为爬虫
        'Referer': 'https://movie.douban.com/'
    }
    url = 'https://movie.douban.com/cinema/nowplaying/dongguan/'

    response = requests.get(url=url,headers=headers)
    ret = response.content.decode('utf-8')
    # print(ret)
    return ret


# 2.对数据进行一定的规则处理
def get_data(text):
    html = etree.HTML(text)

    # 获取正在热映全部数据（ul只有一个）
    ul = html.xpath('//ul[@class="lists"]')[0]

    # 储存多个数据
    movies = []

    # li有多个
    lis = ul.xpath('./li')
    for li in lis:
        title = li.xpath('@data-title')[0]
        score = li.xpath('@data-score')[0]  # 评分
        release = li.xpath('@data-release')[0]  # 时间
        duration = li.xpath('@data-duration')[0]  # 片长
        thumbnail = li.xpath('.//img/@src')[0]

        # 系列化为字典（因为有很多数据，所以要把多个字典放在列表）
        movie = {
            '标题': title,
            '评分': score,
            '时间': release,
            '片长': duration,
            '缩略图': thumbnail,
        }
        movies.append(movie)

    return movies


if __name__ == '__main__':
    text = get_url()
    data = get_data(text)
    print(data)

