import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from myspider.items import TiebaItem

class TiebaCrawlSpider(CrawlSpider):
    name = "crawl_spider"
    allow_domains = "tieba.baidu.com"
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85']
    rules = (
        Rule(LinkExtractor(allow=("/p/.*")), callback="parse_item"),
        Rule(LinkExtractor(allow=("//tieba.baidu.com/f?kw=.*&ie=utf-8&pn=\d+"))),
    )
    count = 0

    def concat_url(request):
        return "https://tieba.baidu.com" + request

    def parse_item(self, response):
        print '-----------------------------'
        self.count = self.count + 1
        print self.count
        item = TiebaItem()
        item['name'] = response.xpath('//a[@alog-group="p_author"]/text()').extract()[0]
        item['images'] = response.xpath('//div[@class="d_author"]/ul[@class="p_author"]/li[@class="icon"]//a[@class="p_author_face "]/img/@data-tb-lazyload').extract()
        return item
