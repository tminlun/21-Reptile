# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/12 0012 21:25'

import requests,json,re

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36',
    'referer': 'https://m.weibo.cn/u/1662575764?uid=1662575764&luicode=10000011&'
               'lfid=1008087a8941058aaf4df5147042ce104568da_-_feed&display=0&retcode=6102'
}


URL = "https://m.weibo.cn/api/container/getIndex?uid=1662575764&luicode=10000011&lfid=1008087a8941058aaf4df5147042ce104568da_" \
              "-_feed&display=0&retcode=6102&type=uid&value=1662575764&containerid=1076031662575764&page={}"

# 保存cookie
s = requests.Session()


# 模拟登陆
def user_login():
    login_url = "https://passport.weibo.cn/sso/login"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36',
        'referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn&display=0&'
                   'retcode=6102&luicode=10000011&lfid=1076031662575764&uid=1662575764'
    }

    data = {
        "username": "123",
        "password": "123",
        "savestate": 1,
        "mainpageflag": 1,
        "entry": "mweibo",
    }

    try:
        response = s.post(login_url, headers=headers, data=data)
        response.raise_for_status()  # 判断请求状态是否为200。是则返回返回正确的内容，否则结合try抛出HttpError异常
    except:
        print("登录失败")
        return False
    print("登录成功")
    return True


def get_url(url):
    global s,HEADERS

    response = s.get(url=url, headers=HEADERS)
    text = json.loads(response.text)
    return text


def parse_page(html):
    ''' 获取用户id '''

    # 1、解析数据
    cards = html['data']['cards']
    # 1.1、第一次请求包含微博导航栏信息，第一次以后请求就只有微博信息
    cards = cards[1:] if len(cards) > 1 else cards['mblog'][0:]
    for card in cards:

        datas = []  # 创建数据列表，最后将它写入csv文件

        # 2.2、解析用户
        mblog = card['mblog']
        user = mblog['user']
        # 2.3、获取用户id
        user_id = user['id']
        datas.append(user_id)

        # 获取用户信息
        try:
            spider_user_info(user_id)
            break
        except:
            print("爬取用户信息失败！ id=%s" % user_id)
            continue

        # 3.1、获取微博内容
        sina_text = mblog['text']
        # 3.2、去掉标签
        # re.S(re.DOTALL)  使 . 匹配包括换行在内的所有字符
        sina_text = re.compile(r'<[^>]+>', re.S).sub(' ', sina_text)
        # 3.3、去掉无用开头
        sina_text = sina_text.replace("周杰伦超话", "").strip()
        datas.append(sina_text)

        # print(user_id)
        # print("=" * 30)



        # 4、爬取用户信息不能太频繁，所以设置一个时间间隔
        import time,random
        time.sleep(random.randint(3, 6))




def spider_user_info(user_id) -> list:
    global s
    '''
    爬取用户信息（需要登录），并将基本信息解析成字典返回
    :param uid:
    :return:  ['用户名', '性别', '地区', '生日']
    '''
    user_info_url = "https://weibo.cn/%s/info" % user_id
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36',
    }

    try:
        response = s.get(url=user_info_url, headers=headers)
        response.raise_for_status()  # 返回正确的数据，如果状态码不是200，则抛出异常
    except:
        print("请求失败！")
        return False
    text = re.findall('<div class="tip">基本信息</div><div class="c">(.*?)</div>', response.text)

    print(text)




def main():
    # 爬取数据前，先登录。登录失败则不不爬取
    if not user_login():
        # 自动调用 user_login
        return "停止爬取"

    for i in range(1, 3):
        url = URL.format(i)
        # 获取网页
        html = get_url(url)

        # 解析网页
        parse_page(html)



if __name__ == '__main__':
    main()

