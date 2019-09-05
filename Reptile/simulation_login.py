# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/8/30 0030 22:57'

'''
自动登录访问授权：
'''

from urllib import request, parse
from http.cookiejar import CookieJar


class SimulationLogin(object):
    def __init__(self):
        # 数据和登录url
        self.da_peng_url = 'http://www.renren.com/880506098/profile'
        self.login_url = 'http://www.renren.com/PLogin.do'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }

    def get_opener(self):
        ''' 获取opener '''
        # 一、登录
        # 1、创建CookieJar对象（发送请求后[request.urlopen(req)]，自动将cookie保存到内存[保存到opener]）
        cookiejar = CookieJar()
        # 2、通过CookieJar，创建HTTPCookieProcess对象：handler
        handler = request.HTTPCookieProcessor(cookiejar)
        # 3、通过handler，创建一个opener对象
        opener = request.build_opener(handler)

        return opener

    def login_renren(self,opener):
        '''
        发送登录的请求
        :param opener:
        :return:
        '''
        # 4、通过opener发送登录的请求（用户名、密码）
        data = {
            "email": "15625873905",
            "password": "15625873905"
        }
        # data需要urlencode编码,并且转为bytes
        data = parse.urlencode(data).encode('utf-8')
        # 登录请求，需要的参数
        req = request.Request(self.login_url, data=data, headers=self.headers)
        # 发送请求,此时使用opener发送请求
        opener.open(req)

    def get_profile(self,opener):
        '''
        获取（个人网页）数据
        :param opener: 已携带cookie的对象
        :return:
        '''
        # 二、获取（个人网页）数据
        # 1、获取数据的时候，不要新建opener对象
        # 而应该使用之前创建的opener，因为之前的opener包含了cookie信息
        # 2、上面的request.Request是发送登录的请求，而这时候我们要获取个人数据
        # 所以要新建个request.Request对象
        req1 = request.Request(self.da_peng_url, headers=self.headers)
        resp = opener.open(req1)

        # 写入数据
        with open('daPeng.html', 'w', encoding='utf-8') as f:
            f.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    # 实例化对象。然后获取opener
    simulation_login = SimulationLogin()
    opener = simulation_login.get_opener()

    # 登录。然后根据opener的cookie信息，获取数据
    simulation_login.login_renren(opener)
    simulation_login.get_profile(opener)

