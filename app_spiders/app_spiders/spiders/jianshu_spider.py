# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from app_spiders.items import AcspiderItem

class NewsSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = [
        'http://www.jianshu.com/',
        'http://www.jianshu.com/recommendations/notes?category_id=56&utm_medium=index-banner-s&utm_source=desktop',
        'http://www.jianshu.com/trending/weekly?utm_medium=index-banner-s&utm_source=desktop',
        'http://www.jianshu.com/trending/monthly?utm_medium=index-banner-s&utm_source=desktop',
        'http://www.jianshu.com/c/e048f1a72e3d?utm_medium=index-banner-s&utm_source=desktop',
        'http://www.jianshu.com/c/80e7d5d15e71?utm_medium=index-jianshu-daily-page&utm_source=desktop'
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'app_spiders.pipelines.ImagePipeline': 100,
            'app_spiders.pipelines.JianshuPipeline': 200,
        }
    }

    rules = (
        Rule(LinkExtractor(allow=("/p/\d+")), callback="parse_item"),
    )

    def parse_item(self, response):
        item = AcspiderItem()
        item['title'] = response.xpath('//div[@class="article"]/h1/text()').extract()[0]
        item['time'] = response.xpath('//div[@class="meta"]/span[@class="publish-time"]/text()').extract()[0]
        item['description'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
        item['author'] = response.xpath('//div[@class="author"]//span[@class="name"]/a/text()').extract()[0]
        item['content'] = self.parse_content(response.xpath('//div[@class="show-content"]'))
        item['url'] = response.url
        return item

    def parse_content(self, response):
        content = response.xpath('./p | .//img')
        return map(self.m_content, filter(self.f_content, content))

    def f_content(self, content):
        if content.xpath('./@data-original-src'):
            return True
        else:
            return content.xpath('string(.)').extract()[0].strip() != ""

    def m_content(self, content):
	content_img = content.xpath('./@data-original-src')
        if content_img:
	    if 'http:' in content_img:
		return {"image": content_img.extract()[0]}
	    else:
            	return {"image": 'http:' + content.xpath('./@data-original-src').extract()[0]}
        else:
            return {"paragraph": content.xpath('string(.)').extract()[0].strip()}
