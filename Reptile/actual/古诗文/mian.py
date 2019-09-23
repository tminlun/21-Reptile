# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/18 0018 13:43'

import requests
import re
import time
import random


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

    }

    response = requests.get(url=url, headers=headers)
    text = response.text
    return text


def parse_page(html):

    modern_datas = []  # 储存所有数据

    re_title = re.compile("""<div\sclass="cont">  # 获取包含标题的父盒子
                    .*?  # 非贪婪  一遇到第一个<b>就停止；否则 一直贪婪到最后一个cont的<b>
                    <b>(.*?)</b>  # 只匹配()的值；必须非贪婪，否则 贪婪最后一个cont的</b>前的所有数据
    """,re.X)  # re.X  正则字符可以注释

    # 标题
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', html, re.DOTALL)  # 默认"."是不匹配空白字符的，re.DOTALL 使其能匹配空白字符
    # print(titles)

    # 朝代  .*? 非贪婪，防止匹配到最后一个
    dynastys = re.findall(r'<p class="source"><a.*?>(.*?)</a>', html, re.DOTALL)

    # 作者
    authors = re.findall(r'<p class="source"><a.*?<a.*?>(.*?)</a>', html, re.DOTALL)

    # 内容
    contsons = re.findall(r'<div class="contson" .*?>(.*?)</div>', html, re.DOTALL)

    context = []  # 保存处理后的内容

    # 过滤内容
    for contson in contsons:
        contson = re.sub(r'<.*?>','',contson).strip()
        context.append(contson)


    # 遇到多个列表，就用zip
    for value in zip(titles, dynastys, authors, context):
        '''
        a = [1,2]  b=[3,4]
        zip(a,b) ==  [
            (1,3),
            (2,4)
        ]
        '''
        # a,b = [1,2]  =>  a=1  b=2
        titles,dynastys,authors,context = value  # 将每个字段提取出来
        pamt = {
            'titles': titles,
            'dynastys': dynastys,
            'authors': authors,
            'context': context,
        }
        # 多个数据
        modern_datas.append(pamt)

    # 储存为csv文件
    save_csv(modern_datas)


# 写入数据
def save_csv(datas):
    import csv

    headers = ['titles','dynastys','authors','context']

    try:
        with open('modern.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            writer.writerows(datas)
            print("保存成功")

    except Exception as e:
        print("保存失败：%s" % e)


def main():
    for i in range(1, 5):

        # 防止封ip
        time.sleep(random.randint(1, 5))
        # 获取url
        url = "https://www.gushiwen.org/default_1.aspx"
        html = get_url(url)
        # 解析数据
        parse_page(html)


if __name__ == '__main__':
    main()

