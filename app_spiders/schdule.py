from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

os.system('scrapy crawl acfun_spider')
# os.system('scrapy crawl jiandan_spider')
os.system('scrapy crawl jianshu_spider')
def job():
    os.system('scrapy crawl acfun_spider')
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def pengfu():
    os.system('scrapy crawl pengfu_spider')
    print('crawl all pengfu.com')


scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=30)
scheduler.add_job(pengfu, 'interval', hours=30)
scheduler.start()
