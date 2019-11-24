# -*- coding: utf-8 -*-

"""
# Save the data
# 需要在setting激活ITEM_PIPELINES
"""


import json

# 旧版本
"""
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("budejie.json", "w", encoding="utf-8")  # w 覆盖

    def open_spider(self,spider):
        '''打开爬虫就执行'''
        print('爬虫开始啦.....')

    def process_item(self, item, spider):
        '''
        储存至文件
        :param item: 爬虫parse方法yield的值  类型为QsbkItem
        '''
        # QsbkItem不能dumps，需要转为dict()
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json + "\n")
        return item

    def close_spider(self,spider):
        '''爬虫关闭时执行'''
        self.fp.close()
        print("爬虫结束啦....")
"""

# 新版本1  JsonItemExporter
"""
from scrapy.exporters import JsonItemExporter
class QsbkPipeline(object):
    # 好处：储存数据是一个满足json格式的数据；坏处：储存量大耗内存(先储存到内容，最后统一写入磁盘)
    def __init__(self):
        # wb 以二进制打开；因为JsonItemExporter要以byte类型储存
        self.fp = open("budejie.json", "wb")
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")

        # [ ==> 数据
        self.exporter.start_exporting()

    def open_spider(self, spider):
        '''打开爬虫就执行'''
        print('爬虫开始啦.....')

    def process_item(self, item, spider):
        '''保存数据  把数据添加到列表'''
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        '''爬虫关闭时执行'''

        # 结束保存  # 数据 ==> ]  
        self.exporter.finish_exporting()

        # 关闭文件
        self.fp.close()
        print("爬虫结束啦....")
"""

# 新版本2  JsonLinesItemExporter
from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline(object):
    # 好处：每次调用export_item就把数据储存到磁盘，不消耗内存。坏处：不满足json数据格式
    def __init__(self):
        # wb 以二进制打开；因为JsonItemExporter要以byte类型储存
        self.fp = open("budejie.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")

    def open_spider(self, spider):
        '''打开爬虫就执行'''
        print('爬虫开始啦.....')

    def process_item(self, item, spider):
        '''保存数据'''
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        '''爬虫关闭时执行'''
        # 关闭文件
        self.fp.close()
        print("爬虫结束啦....")
