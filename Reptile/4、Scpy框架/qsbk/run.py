# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/11/21 0021 19:31'

'''
运行scrapy命令
'''
from scrapy import cmdline

cmdline.execute("scrapy crawl qiumeimei".split())  # 相等于 cmdline.execute(["scrapy", "crawl", "qiumeimei"])
