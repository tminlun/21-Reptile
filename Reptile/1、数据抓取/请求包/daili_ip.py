# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/3 0003 17:06'


'''
requests使用代理ip
'''
import requests,random

proxies={
    'http': '58.253.154.89:9999'
}

res = requests.get(url='http://httpbin.org/ip',proxies=proxies)

print(res.text)