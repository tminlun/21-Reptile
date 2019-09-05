# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/3 0003 17:32'

'''
session：一个会话对象，自动储存cookie
'''

import requests


def session_login():
    login_url = 'http://www.renren.com/PLogin.do'
    # headers信息和参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    # 参数
    data = {
        "email": "15625873905",
        "password": "15625873905"
    }

    # # 使用代理ip
    # proxies = {
    #     'http':'140.143.152.93:1080'
    # }

    # 储存cookie
    session = requests.session()

    # 使用session登录
    session.post(login_url, data=data, headers=headers)  # proxies=proxies)

    return session


def daPeng_data(session):
    da_peng_url = 'http://www.renren.com/880506098/profile'
    # 使用session：储存了cookie，获取数据
    response = session.get(da_peng_url)

    with open("ren.html", "w", encoding="utf-8") as f:
        f.write(response.text)


if __name__ == '__main__':
    session = session_login()
    daPeng_data(session)