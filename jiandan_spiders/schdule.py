from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

os.system('scrapy crawl jiandan_spider')

def jian_dan_all():
    os.system('scrapy crawl jiandan_spider')
    print('crawl all jandan.net')

def jian_dan_new():
    os.system('scrapy crawl new_jiandan_spider')
    print('crawl newest jandan.net')

scheduler = BlockingScheduler()
scheduler.add_job(jian_dan_new, 'interval', hours=2)
scheduler.start()
