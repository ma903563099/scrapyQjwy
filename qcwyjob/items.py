# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QcwyjobItem(scrapy.Item):

    firmName = scrapy.Field()
    trade = scrapy.Field()
    firmScale = scrapy.Field()
    workAddress = scrapy.Field()
    firmAddress = scrapy.Field()
    pub_time = scrapy.Field()
    salary = scrapy.Field()
    edu = scrapy.Field()
    workexper = scrapy.Field()
    workName = scrapy.Field()
    workdesc = scrapy.Field()
    workstatus = scrapy.Field()

