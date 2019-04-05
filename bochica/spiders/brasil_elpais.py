"""
.. module:: brasil_elpais
   :synopsis: Scrapy crawler for the website 'brasil elpais'.
.. moduleauthor:: Benardi <github.com/Benardi>
"""

# -*- coding: utf-8 -*-
import json

import scrapy

from bochica.items import ArticleItem
from bochica.items import ArticleCommentItem



def parse_article(response):
    
    """ Builds ArticleItem from an article page html.

    Parsed html of an article page and creates an ArticleItem.

    :param class 'scrapy.http.response.html.HtmlResponse' \
           response: scrapy response object.

    :return: python dictionary in ArticleItem format

    :rtype: dict
    """
    item = ArticleItem()
    item['url'] = response.request.url
    item["section"] = response.css("div.seccion-migas span span::text").get()
    item["title"] = response.css("h1::text").get()
    item["subtitle"] = response.css("h2::text").get()
    item["date"] = response.css("time::attr(datetime)").get()
    item["author"] = response.css("span.autor-nombre a::text").get()
    item["text"] = locate_text(response)

    return item 

def locate_text(response):

   """ Deduces article page format and extract its text.

   Deduces article page format and extract its text accordingly.

   :param <class 'scrapy.http.response.html.HtmlResponse'> \
          response: scrapy response object.

   :return: article page text

   :rtype: <class 'scrapy.http.response.html.HtmlResponse'> 
   """
   text = '' 
   p_res = response.css("div.articulo-cuerpo p::text").getall()
   p_res_text = ''.join(p_res) 

   span_res = response.css("div.articulo-cuerpo span::text").getall()
   span_res_text = ''.join(span_res) 
   
   galeria_res = response.css("div.articulo-galeria figcaption \
                              span.foto-texto::text").getall()
   galeria_res_text = ''.join(galeria_res)

   if len(p_res_text) >= len(span_res_text) and \
      len(p_res_text) >= len(galeria_res_text):
        text = p_res
   
   elif len(span_res_text) >= len(p_res_text) and \
      len(span_res_text) >= len(galeria_res_text):
        text = span_res

   else:
        text = galeria_res
   
   return text


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
            if url :
                url = "https:" + url 
                yield response.follow(url, callback=parse_article)
   

