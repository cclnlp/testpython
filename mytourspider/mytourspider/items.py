# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MytourspiderItem(scrapy.Item):
    # define the fields for your item here like:
    href =scrapy.Field()
    title  =scrapy.Field()
    address = scrapy.Field()
    picture = scrapy.Field()
    ticket = scrapy.Field()
    abstract = scrapy.Field()
    time = scrapy.Field()
    traffic = scrapy.Field()
    surrounding = scrapy.Field()



