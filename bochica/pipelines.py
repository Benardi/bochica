# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings

from bochica.items import RiLab01Item
from bochica.items import RiLab01CommentItem

class RiLab01Pipeline(object):
    client = None;
    db = None;

    def open_spider(self, spider):
        # init client mongo
        self.client = MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        # set database
        self.db = self.client[settings['MONGODB_DB']]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, RiLab01Item):
            self.db[spider.name].insert_one(item)
        elif isinstance(item, RiLab01CommentItem):
            self.db[spider.name + 'Comments'].insert_one(dict(item))
        else:
            self.db[spider.name + 'MetaData'].insert_one(item)
        return item
