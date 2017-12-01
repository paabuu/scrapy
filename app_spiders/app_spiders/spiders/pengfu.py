# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from app_spiders.items import PengfuItem

import redis

class PengfuSpider(Spider):
    name = 'pengfu_spider'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    custom_settings = {
        'ITEM_PIPELINES': {
            'app_spiders.pipelines.PengfuPipeline': 100,
        }
    }
    start_urls = ['https://www.pengfu.com/qutu_1.html']
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers)

    def parse(self, response):
        item = PengfuItem()
        urls = response.xpath('//div[@class="content-img clearfix pt10 relative"]/img/@jpgsrc | //div[@class="content-img clearfix pt10 relative"]/img/@gifsrc').extract()
        item['image_urls'] = urls;
        yield item
