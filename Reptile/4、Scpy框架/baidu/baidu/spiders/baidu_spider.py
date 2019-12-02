# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BaiduSpiderSpider(CrawlSpider):
    name = 'baidu_spider'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python%E5%BC%80%E5%8F%91&page=1&ka=page-prev']

    rules = (
        # 获取所有页码（page）的链接
        Rule(LinkExtractor(allow=r'page=\d+'),callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'job_detail/.*?\.html'), callback='parse_detail')

    )

    def parse_item(self, response):
        li_list = response.xpath('//div[@class="job-list"]/ul/li')
        for li in li_list:
            job_title = li.xpath('.//div[@class="job-title"]/text()').extract_first()
            print(job_title)
            yield job_title

    def parse_detail(self, response):
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        print(job_desc)
        yield job_desc
