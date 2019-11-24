# -*- coding: utf-8 -*-

# resemble Djagno Models

import scrapy


class QsbkItem(scrapy.Item):
    # Field() is fixation
    author = scrapy.Field()
    content = scrapy.Field()

