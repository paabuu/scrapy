from scrapy.spiders import Spider
from myspider.items import DoubanBooksItem
from scrapy import Request

class DoubanBookSpider(Spider):
    name =  "douban_book"
    headers = {
        'Cookie': 'bid=J1xL8IOOHTo; __ads_session=+5oAwa8w/wjQ4MQgJgA=; ap=1; _pk_id.100001.3ac3=835437a5f59eac09.1509430232.1.1509430232.1509430232.; __utma=30149280.1675989017.1509418719.1509418719.1509430232.2; __utmc=30149280; __utmz=30149280.1509418719.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=81379588.836664551.1509430232.1509430232.1509430232.1; __utmc=81379588; __utmz=81379588.1509430232.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanBooksItem()

        # books = response.xpath('//div[@class="article"]/div[@class="indent"]//tr[@class="item"]')
        # for book in books:
        #     title = book.xpath('.//div[@class="pl2"]/a/@title').extract()
        #     info = book.xpath('.//p[@class="pl"]/text()').extract()
        #     quote = book.xpath('.//p[@class="quote"]/span/text()').extract()
        #     if len(title) > 0:
        #         item['book_name'] = title[0]
        #         item['info'] = info[0]
        #         item['quote'] = quote[0]
        #         yield item
        images = response.xpath('//div[@class="article"]/div[@class="indent"]//tr[@class="item"]//a[@class="nbg"]/img/@src').extract()
        if len(images) > 0:
            item['image_urls'] = images
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        if next_url:
            print(next_url, 'xxxxxxxxxxxxxxxxxxxxxxxxxx')
            next_url = 'https://book.douban.com/top250' + next_url
            yield Request(next_url, headers=self.headers)
