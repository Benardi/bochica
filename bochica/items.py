# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    '''
    The ArticleItem represents the fundamental \
    fields of an article.
    '''
    title = scrapy.Field()
    subtitle = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    section = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()

class ArticleCommentItem(scrapy.Item):
    '''
    The ArticleCommentItem represents the fundamental \
    fields of an article comment.
    '''
    id_article = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
