# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HSFL_LNN_Item(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    preview = scrapy.Field()
    image = scrapy.Field()

    course = scrapy.Field()
    study_course = scrapy.Field()
    study_course_id = scrapy.Field()