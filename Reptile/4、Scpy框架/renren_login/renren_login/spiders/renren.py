# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['http://www.renren.com/']
    start_urls = ['http://http://www.renren.com//']

    # 重写start_requests才能使用post请求
    def start_requests(self):
        pass

    def parse(self, response):
        pass
