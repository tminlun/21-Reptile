# -*- coding: utf-8 -*-
"""
需要激活setting的 DEFAULT_REQUEST_HEADERS；并将ROBOTSTXT_OBEY改成False
"""
import scrapy

from scrapy.http.response.html import HtmlResponse  # 可以执行xpath, css
from scrapy.selector.unified import SelectorList

from qsbk.items import QsbkItem


class QiumeimeiSpider(scrapy.Spider):
    # 运行爬虫的名称
    name = 'qiumeimei'

    # 域名，只爬取此域名的数据
    allowed_domains = ['budejie.com']

    # 从这个url开始爬取
    start_urls = ['http://www.budejie.com/45']

    # 公共域名
    base_domains = "http://www.budejie.com/"

    def parse(self, response):
        """
        提取数据
        :param response: 下载完成数据；类型为HtmlResponse
        """
        # response.xpath()  提取出来的数据类型为SelectorList
        liList = response.xpath('//div[@class="j-r-list"]/ul/li')
        for li in liList:
            # Selector: get()将Selector转换为uncode
            author = li.xpath('.//div[@class="u-txt"]/a/text()').get()
            content = li.xpath('.//div[@class="j-r-list-c"]/div[@class="j-r-list-c-desc"]/a/text()').getall()
            content = "".join(content).strip()

            # 规范，固定传递指定参数
            item = QsbkItem(author=author, content=content)
            yield item  # ==> itmes.append(item)

        '''
        爬取下一页：获取"下一页"的链接，再次回调parse方法。直到无"下一页"链接则return方法
        '''
        next_url = response.xpath('//div[@class="j-page"]//a[@class="pagenxt"]/@href').get()
        if not next_url:
            return
        elif int(next_url) == 51:
            # 51页无数据
            print("最后一页啦  %s" % next_url)
            return
        else:
            # 返回当前请求给parse()；不能用return（会停止执行parse方法）
            yield scrapy.Request(self.base_domains + next_url, callback=self.parse)

