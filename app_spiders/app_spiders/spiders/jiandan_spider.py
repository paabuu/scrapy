# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from app_spiders.items import JianDanItem

class JianDanSpider(Spider):
    name = 'jiandan_spider'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }

    custom_settings = {
        'ITEM_PIPELINES': {
            'app_spiders.pipelines.JianDanPipeline': 100,
        }
    }

    def start_requests(self):
        url = 'http://jandan.net/pic/page-1#comments'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = JianDanItem()
        urls = response.xpath('//ol[@class="commentlist"]//a[@class="view_img_link"]/@href').extract()
        item['image_urls'] = urls;
        yield item

        next_url = response.xpath('//a[@class="next-comment-page"]/@href').extract()
        if next_url:
            next_url = 'http:' + next_url[0]
            yield Request(next_url, headers=self.headers)

# import json
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LinkExtractor
# from scrapy.http import Request,FormRequest
#
# from app_spiders.items import JianDanItem
#
# class NewsSpider(CrawlSpider):
#     name = 'jiandan_spider'
#     allowed_domains = ['jandan.net']
#     start_urls = ('http://jandan.net/pic',)
#
#     rules = (
#         Rule(LinkExtractor(allow=("jandan.net/pic/page-\d+\S+"))),
#         Rule(LinkExtractor(restrict_xpaths='//span[@id="nav_prev"]/a'), callback="parse_item"),
#     )
#
#     def start_requests(self):
#         for i, url in enumerate(self.start_urls):
#             yield Request(url, meta = {'cookiejar': i}, headers = { 'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" })
#
#     def parse_item(self, response):
#         item = JianDanItem()
#         item['image_urls'] = response.xpath('//ol[@class="commentlist"]//a[@class="view_img_link"]/@href').extract()
#         print '------------'
#         print response.url
#         print item
#         print '------------'
#         return item
