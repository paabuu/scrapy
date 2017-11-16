# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from app_spiders.items import JianDanItem

class NewJianDanSpider(Spider):
    name = 'new_jiandan_spider'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }

    custom_settings = {
        'ITEM_PIPELINES': {
            'app_spiders.pipelines.JianDanPipeline': 100,
        }
    }

    start_urls = ['http://jandan.net/pic', 'http://jandan.net/ooxx']
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers)

    def parse(self, response):
        item = JianDanItem()
        urls = response.xpath('//ol[@class="commentlist"]//a[@class="view_img_link"]/@href').extract()
        item['image_urls'] = urls;
        yield item
