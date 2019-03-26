# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RiLab01Item(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    sub_title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    section = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()

class RiLab01CommentItem(scrapy.Item):
    id_article = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
