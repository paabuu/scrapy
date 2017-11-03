# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from acspider.items import AcspiderItem

class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['acfun.cn']
    start_urls = ['http://acfun.cn/v/list110/index_1.htm']

    rules = (
        Rule(LinkExtractor(allow=("/a/ac.*")), callback="parse_item"),
        # Rule(LinkExtractor(allow=("index_\d+.htm")), follow=True)
    )

    def parse_item(self, response):
        item = AcspiderItem()
        item['title'] = response.xpath('//span[@class="txt-title-view_1"]/text()').extract()[0]
        item['time'] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item['content'] = self.parse_content(response)

        return item

    def parse_content(self, response):
        contents = response.xpath('//div[@id="area-player"]/p' or '/div[@class="article-content"]/p')
        return map(self.m_content, filter(self.f_content, contents))

    def f(self, item):
        return item.strip() != ''

    def m(self, item):
        return {"paragraph": item.strip()}

    def f_content(self, content):
        if content.xpath('.//img/@src'):
            return True
        else:
            return content.xpath('string(.)').extract()[0].strip() != ""

    def m_content(self, content):
        if content.xpath('.//img/@src'):
            return {"image": content.xpath('.//img/@src').extract()[0]}
        else:
            return {"paragraph": content.xpath('string(.)').extract()[0].strip()}
