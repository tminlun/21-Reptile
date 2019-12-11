# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['developers.weixin.qq.com']
    start_urls = ['https://developers.weixin.qq.com']

    BASE_ALLOWED_DETAIL = "https://developers.weixin.qq.com/community/develop/doc/"

    """
      这个Rule啊其实就是为了爬取全站内容的写法
    :allow：这里用的是re过滤，我们其实就是start_urls加上我们这个匹配到的具体链接下的内容
    ：follow=True ：跟进；爬取所有以start_urls开头的url
    ：follow=False ：只爬取当前的url，防止爬取推荐文章
    ：LinkExtractor: 筛选出来我们需要爬取的链接
    ：callback：我们拿到可以爬取到的url后，要执行的方法
    """

    rules = (
        # 这个Rule只获取详情的url，所以不需要callback（解析方法）
        # 它会自动将爬取下面指定的详情url，发送给下面的Rule
        Rule(LinkExtractor(allow=r'.+/community/ngi/question/list?page=\d+&tag=new&blo'
                  'cktype=30&openid=&random=0.8950513528607165/'),
            follow=True,callback='parse_item'),

        # # 这个Rule才是获取详情数据
        # Rule(LinkExtractor(allow=r'.+community/develop/doc/.*?'),
        #      callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        # TextResponse转换为srt数据类型
        response = response.text
        #  将json转为py数据类型
        res = json.loads(response)

        # 获取数据
        rows = res['data']['rows']
        print(type(response))
        for row in rows:
            docId = row['DocId']
            docId = self.BASE_ALLOWED_DETAIL + docId
            # print(docId)
    #
    # def parse_item(self, response):
    #     list_title = response.xpath('//span[@class="post_title_content"]/text()').get()
    #     print(list_title)
