# -*- coding: utf-8 -*-
import json
import pdb

import scrapy
import pandas

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
        articles = response.css("div.articulo__interior")
     
        for article in articles:
            url = article.css("h2.articulo-titulo a::attr(href)").get()
            if url is not None:
                url = "https:" + url 
                yield response.follow(url, callback=self.parse_article)


        
    def parse_article(self, response):
        url = response.request.url
        page_index = {}
        page_index[url] = {}

        page_index[url]["section"] = response.css("div.seccion-migas span span::text").get()
        page_index[url]["title"] = response.css("h1::text").get()
        page_index[url]["subtitle"] = response.css("h2::text").get()
        page_index[url]["time"] = response.css("time::attr(datetime)").get()
        page_index[url]["author"] = response.css("span.autor-nombre a::text").get()
        page_index[url]["text"] = response.css("div.articulo-cuerpo p::text").getall()
    
        return page_index
