# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import scrapy

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class Top250Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print item
        for image_url in item['image_urls']:
            print image_url
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]      # ok判断是否下载成功
        if not image_paths:
            raise DropItem("Item contains no images")
        #item['image_paths'] = image_paths
        return item
