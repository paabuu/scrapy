import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class TiebaCrawlSpider(CrawlSpider):
    name = "crawl_spider"
    allow_domains = "tieba.baidu.com"
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E6%8A%97%E5%8E%8B&fr=search']

    rules = (
        Rule(LinkExtractor(allow=("/p/\d+")), callback="parse_item"),
        Rule(LinkExtractor(allow=("//tieba.baidu.com/f?kw=%E6%8A%97%E5%8E%8B&ie=utf-8&pn=\d+"))),
    )

    def concat_url(request):
        return "https://tieba.baidu.com" + request

    def parse_item(self, response):
        item = scrapy.Item()

        item['images'] = response.xpath('//ul[@class="p_author"]//img/@src').extract()

        return item
