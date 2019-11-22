# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class QiumeimeiSpider(scrapy.Spider):
    # 运行爬虫的名称
    name = 'qiumeimei'

    # 域名，只爬取此域名的数据
    allowed_domains = ['budejie.com']

    # 从这个url开始爬取
    start_urls = ['http://www.budejie.com/1']

    def parse(self, response):
        """
        提取数据
        :param response: 下载完成数据；并继承HtmlResponse
        """
        # print("="*30)
        # print(type(response))
        # print("=" * 30)

        # type  SelectorList
        liList = response.xpath('//div[@class="j-r-list"]/ul/li')
        for li in liList:
            # Selector: get()将Selector转换为uncode
            author = li.xpath('.//div[@class="u-txt"]/a/text()').get()
            content = li.xpath('.//div[@class="j-r-list-c"]/div[@class="j-r-list-c-desc"]/a/text()').getall()
            content = "".join(content).strip()

            data_dict = {
                'author': author,
                'content': content,
            }
            yield data_dict
