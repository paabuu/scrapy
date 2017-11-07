from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

os.system('/Users/yangwenjie/Desktop/scrapy_test/env/bin/scrapy crawl acfun_spider')

def job():
    os.system('/Users/yangwenjie/Desktop/scrapy_test/env/bin/scrapy crawl acfun_spider')
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=1)
scheduler.start()
