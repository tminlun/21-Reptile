# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/19 0019 14:40'

import requests
import re
from lxml import etree

import csv
import json
import time

'''
查看requests 编码方式：
    import chardet
    print(chardet.detect(r.content))
'''


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

        # 爬取评论，需要的data_id
        time.sleep(1)
        re_data_id = re.search('\d+', url)
        data_id = re_data_id.group()
        parse_commit(data_id)

        # 文章详情的路由
        url = 'http://www.budejie.com' + url
        urls.append(url)
    return urls


# 解析详情url的数据
def parse_detail(text):
    html = etree.HTML(text)
    head_portrait = html.xpath('//div[@class="j-list-user"]//img/@data-original')[0]  # 头像

    author = html.xpath('//div[@class="u-txt"]/a/text()')[0]  # 作者名称

    up_time = html.xpath('//div[@class="u-txt"]/span[contains(@class,"u-time")]/text()')[0]
    title = html.xpath('//div[@class="j-r-list-c-desc"]/h1/text()')[0]  # 文章标题

    photo = html.xpath('//div[@class="j-r-list-c-img"]/img/@src')[0]  # 文章图片

    like_nums = html.xpath('//li[@class="j-r-list-tool-l-up"]//span/text()')[0]  # 点赞数

    article = [{
        '头像': head_portrait,
        '作者名称': author,
        '发表时间': up_time,
        '文章标题': title,
        '文章图片': photo,
        '点赞数': like_nums,
    }]
    headers = ['头像', '作者名称', '发表时间', '文章标题', '文章图片', '点赞数']

    # write_csv(article, 'article.csv',headers)


def write_csv(articles, name_path,headers):
    # import pandas as pd
    # num = 1
    #
    # data = pd.DataFrame(articles)
    # # 写入csv文件,'a+'是追加模式
    # try:
    #     if num == 1:
    #         data.to_csv(name_path, header=headers, index=False, mode='a+', encoding='utf-8')
    #     else:
    #         data.to_csv(name_path, header=False, index=False, mode='a+', encoding='utf-8')
    #         num = num + 1
    # except UnicodeEncodeError:
    #     print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

    with open(name_path, 'w+', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, headers)  # 传递两个参数：文件和标题(但标题需手动添加)
        writer.writeheader()  # 手动加入标题
        writer.writerows(articles)


commits = []
 # 获取评论
def parse_commit(data_id):

    # 头部
    headers = {
        'referer': 'http://www.budejie.com/detail-29745738.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    # url
    commit_url = 'http://api.budejie.com/api/api_open.php?a=datalist&per=5&c=comment&hot=1' \
                 '&appname=www&client=www&device=pc&data_id={data_id}' \
                 '&page=1&callback=jQuery180023931951193588374_1569319796082&_=1569319796209'.format(data_id=int(data_id))

    r = requests.get(commit_url, headers=headers)
    # text = r.content.decode('unicode-escape')[42:-1]
    # 先用'ascii'数据，再已'utf-8'编码写入文件
    text = r.content.decode('ascii')[42:-1]

    # 类型转换
    try:
        text_json = json.loads(text)
        # 数据
        datas = text_json['data']

        for data in datas:
            content = data['content']  # 内容
            ctime = data['ctime']  # 评论时间
            # 评论作者
            user = data['user']
            user_name = user['username']  # 评论作者

            # 性别
            sex = str(user['sex']) if 'sex' in user else '没有性别'
            if sex == 'm':
                sex = '男'
            else:
                sex = '女'

            # 作者头像
            profile_image = user['profile_image']

            # 是否vip
            is_vip = user['is_vip']
            if is_vip == False:
                is_vip = '否'
            else:
                is_vip = '是'

            commit = {
                '内容': content,
                '评论时间': ctime,
                '评论作者': user_name,
                '性别': sex,
                '作者头像': profile_image,
                '是否vip': is_vip
            }

            commits.append(commit)
            break
    except:
        pass
    # 写入文件
    headers = [u'内容',u'评论时间',u'评论作者',u'性别',u'作者头像',u'是否vip']
    write_csv(commits, 'commits.csv', headers)



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

        # break  # 获取一条



if __name__ == '__main__':
    main()



