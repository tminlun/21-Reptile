# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/7 0007 13:54'

'''
腾讯招聘：
    1、先在列表爬取，职位详情的url
    2、在通过url获取数据
'''
import requests, json, re
from lxml import etree


list_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1567835517884&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&' \
           'attrId=&keyword=python&pageIndex={}&pageSize=10&language=zh-cn&area=cn'

detail_url = 'https://careers.tencent.com/tencentcareer/api/post/B' \
             'yPostId?timestamp=1567841460257&postId={}&language=zh-cn'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36',
    'Referer': 'https://careers.tencent.com/search.html?index=4&keyword=python'
}


def get_url(url):
    '''获取url'''
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code != 200:
        return False
    text = response.content.decode('utf-8')

    return text


# 获取职位详情的url
def get_detail_url(text):
    '''
        :param text: 列表的网页
    '''

    PostIds = []  # 储存url

    # 返回的事json数据，所以进行反序列化
    text = json.loads(text)

    # 获取url
    Posts = text['Data']['Posts'] if 'Posts' in text['Data'] else None

    if Posts is None:
        return False

    for post in Posts:
        # 遍历列表
        PostId = post['PostId'] if 'PostId' in post else ''
        if not PostId:
            continue

        if len(PostId) != 19:
            continue

        PostIds.append(PostId)

    return PostIds


# 解析详情页面数据
def parse_detail(url):

    position = {}

    # 获取页面
    text = get_url(url)
    text = json.loads(text)

    # 规则页面
    Data = text['Data']
    title = Data['RecruitPostName']
    city = Data['LocationName']
    category = Data['CategoryName']
    pub_time = Data['LastUpdateTime']
    responsibility = Data['Responsibility'].replace("\n", "").strip() # 工作职责
    requirement = Data['Requirement'].replace("\n", "").strip() # 工作要求

    position = {
        '名称': title,
        '城市': city,
        '类别': category,
        '发布时间': pub_time,
        '工作职责': responsibility,
        '工作要求': requirement,
    }
    print(position)

    return position


def main():
    positions = []  # 储存所有数据

    for i in range(1, 4):
        # 获取列表url
        url = list_url.format(i)
        text = get_url(url)

        # 详情的url
        postId = get_detail_url(text)

        # 遍历详情的url
        for id in postId:
            url = detail_url.format(id)
            position = parse_detail(url)
            positions.append(position)

            import time
            time.sleep(0.5)

    print(positions)
    return positions


if __name__ == '__main__':
    main()
