from scrapy.spiders import Spider
from tieba.items import TiebaItem
from scrapy import Request

class TiebaSpider(Spider):
    name = "tieba_spider"
    domain_url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E6%8A%97%E5%8E%8B&fr=search'
    def start_requests(self):
        url = self.domain_url
        yield Request(url)


    def parse(self, response):
        item = TiebaItem()

        tiezis = response.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract()
        print '------------------------------'
        print '------------------------------'
        print '------------------------------'
        print tiezis
        for tiezi in tiezis:
            item['pages'] = "https://tieba.baidu.com/" + tiezi
            yield item

        next_url = "http:" + response.xpath('//a[@class="next pagination-item "]/@href').extract()[0]
        if next_url:
            yield Request(next_url)
