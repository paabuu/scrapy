# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()

class DoubanBooksItem(scrapy.Item):
    book_name = scrapy.Field()
    info = scrapy.Field()
    quote = scrapy.Field()
    image_urls = scrapy.Field()
