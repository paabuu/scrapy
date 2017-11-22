# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time
import codecs
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import scrapy

from pymongo import MongoClient
import redis
r = redis.Redis(host="127.0.0.1", port=6379, db=0)

client = MongoClient('localhost', 27017)
db = client.acfun
collection = db['news']

class JianshuPipeline(object):
    def process_item(self, item, spider):
        publish_time = item['time']
        item['time'] = publish_time.encode('utf8').replace('.', '-')

        if r.sismember('urls', item['url']):
            return item
        else:
            r.sadd('urls', item['url'])
            db.news.insert({
                "title": item['title'],
                "publish_time": item['time'],
                "content": item['content'],
                "description": item['description'],
                "origin_site": '简书',
                "create_time": time.time(),
                "cover_image": '',
                "author": item['author']
            })
            return item

class JianDanPipeline(object):
    def process_item(self, item, spider):
        for image_url in item['image_urls']:
            if r.sismember('jiandan_pic', image_url):
                return item
            else:
                r.sadd('jiandan_pic', image_url)
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for c in item['content']:
            if c.has_key('image'):
                yield scrapy.Request(c['image'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]      # ok判断是否下载成功
        if not image_paths:
            # raise DropItem("Item contains no images")
            return item
        else:
            #item['image_paths'] = image_paths
            for index, i in enumerate(item['content']):
                 if i.has_key('image'):
                    item['content'][index]['image'] = 'https://ipabu.com/images/insert/' + image_paths.pop(0)
        if len(item['content']) > 0:
            return item
