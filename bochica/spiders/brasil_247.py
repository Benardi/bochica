# -*- coding: utf-8 -*-
import scrapy
import json

from bochica.items import RiLab01Item
from bochica.items import RiLab01CommentItem


class Brasil247Spider(scrapy.Spider):
    name = 'brasil_247'
    allowed_domains = ['brasil247.com']
    start_urls = []

    def __init__(self, *a, **kw):
        super(Brasil247Spider, self).__init__(*a, **kw)
        with open('seeds/brasil_247.json') as json_file:
                data = json.load(json_file)
        self.start_urls = list(data.values())

    def parse(self, response):
        #
        # inclua seu código aqui
        #
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        #
        #
        #
