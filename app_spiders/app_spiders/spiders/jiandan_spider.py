# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from app_spiders.items import JianDanItem

class NewsSpider(CrawlSpider):
    name = 'jiandan_spider'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/pic']

    rules = (
        Rule(LinkExtractor(allow=("/a/ac\d+")), callback="parse_item"),
        Rule(LinkExtractor(allow=("index_\d+.htm")), follow=True)
    )

    def parse(self, response):
        item = 
    
    def parse_item(self, response):
        item = AcspiderItem()
        
        return item

