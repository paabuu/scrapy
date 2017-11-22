from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

os.system('scrapy crawl acfun_spider')
# os.system('scrapy crawl jiandan_spider')
os.system('scrapy crawl jianshu_spider')
def job():
    os.system('scrapy crawl acfun_spider')
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def jian_dan_all():
    os.system('scrapy crawl jiandan_spider')
    print('crawl all jandan.net')

def jian_dan_new():
    os.system('scrapy crawl new_jiandan_spider')
    print('crawl newest jandan.net')

def jianshu():
    os.system('scrapy crawl jianshu_spider')

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=30)
# scheduler.add_job(jian_dan_all, 'interval', hours=1)
#scheduler.add_job(jian_dan_new, 'interval', minutes=3)
scheduler.add_job(jianshu, 'interval', hours=1)
scheduler.start()
