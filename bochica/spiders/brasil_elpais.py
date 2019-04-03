# -*- coding: utf-8 -*-
import scrapy
import json

from bochica.items import RiLab01Item
from bochica.items import RiLab01CommentItem


class BrasilElpaisSpider(scrapy.Spider):
    name = 'brasil_elpais'
    allowed_domains = ['brasil.elpais.com']
    start_urls = []

    def __init__(self, *a, **kw):
        super(BrasilElpaisSpider, self).__init__(*a, **kw)
        with open('seeds/brasil_elpais.json') as json_file:
                data = json.load(json_file)
        self.start_urls = list(data.values())

    def parse(self, response):
        #
        # inclua seu código aqui
        #
#        page = response.url.split("/")[-2]
#        filename = 'quotes-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#        self.log('Saved file %s' % filename)
        for article in response.css("div.articulo__interior"):
            yield {
                'url': article.css("h2.articulo-titulo a::attr(href)").get(),             
                'title': article.css("h2.articulo-titulo a::text").get(),
                'time': article.css("div.articulo-metadatos time::attr(datetime)").get(),
                'author': article.css("div.articulo-metadatos a::text").get(),
                'subtitle': article.css("p.articulo-entradilla::text").get() 	
         }
        #
        #
        #
