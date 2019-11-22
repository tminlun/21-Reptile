# -*- coding: utf-8 -*-

# Used to store the "item.py" model to a local disk
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QsbkPipeline(object):

    def __int__(self):
        self.fp = open("budejie.json", "w", encoding="utf-8")

    def open_spider(self,spider):
        '''打开爬虫就执行'''
        print('爬虫开始啦.....')

    def process_item(self, item, spider):
        '''
        :param item: 爬虫parse方法yield的值
        '''
        item_json = json.dumps(item, ensure_ascii=False)
        self.fp.write(item_json + "\n")
        return item

    def close_spider(self,spider):
        '''爬虫关闭时执行'''
        # self.fp.close()
        print("爬虫结束啦....")
