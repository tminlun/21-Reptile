# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/8/30 0030 19:48'

'''
1、ip代理：
    百度：请求url
    代理：代理服务器
    本机ip访问代理，代理再访问百度。此时百度只会识别代理的ip
    
2、测试网站：http://httpbin.org/ip。它会返回访问它的ip地址
'''

from urllib import request
import random

url = 'https://httpbin.org/get'

# 未使用代理
# req = request.urlopen(url)
# print(req.read().decode('utf-8'))  # "origin": "27.37.117.226"

# 使用代理
proxy_list = [
    {"HTTPS": "49.51.68.122:1080"},
    {"HTTP": "125.110.96.85:9000"},
    {"HTTPS": "123.139.56.238:9999"}
]
# 随机ip
proxy = random.choice(proxy_list)

# 1、使用ProxyHandler，传入代理ip，创建一个handler
handler = request.ProxyHandler({"HTTPS": "49.51.68.122:1080"})
# 2、使用handler，创建一个opener
opener = request.build_opener(handler)

# 3、用opener发送一个请求
resp = opener.open(url).read().decode('utf-8')

print(resp)
