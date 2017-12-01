# -*- coding: utf-8 -*-

# Scrapy settings for app_spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'app_spiders'

SPIDER_MODULES = ['app_spiders.spiders']
NEWSPIDER_MODULE = 'app_spiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'app_spiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'app_spiders.middlewares.AppSpidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'app_spiders.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'app_spiders.pipelines.AppSpidersPipeline': 300,
#}
# ITEM_PIPELINES = {
   # 'app_spiders.pipelines.AcspiderPipeline': 303,
   # 'app_spiders.pipelines.ImagePipeline': 301,
   # 'app_spiders.pipelines.JianDanSpider': 302,
   # 'app_spiders.pipelines.JsonWithEncodingPipeline': 304
# }
IMAGES_STORE = '/Users/yangwenjie/Desktop/scrapy_test/images'
# IMAGES_STORE = '/root/ipabu_app/images/insert'
DOWNLOAD_TIMEOUT = 60
DOWNLOAD_DELAY = 2
MEDIA_ALLOW_REDIRECTS = True
# LOG_LEVEL = 'ERROR'
# DOWNLOADER_MIDDLEWARES = {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,}

# DOWNLOADER_MIDDLEWARES = {
# #    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
#     # 'app_spiders.middlewares.RandomUserAgent': 1,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     'app_spiders.middlewares.ProxyMiddleware': 100,
# }
# PROXIES = [
#     {'ip_port': '113.110.111.161:808', 'user_pass': ''},
#     {'ip_port': '182.34.49.9:808', 'user_paSss': ''},
#     {'ip_port': '61.135.217.7:80', 'user_pass': ''},
#     {'ip_port': '110.72.34.222:8123', 'user_pass': ''},
#     {'ip_port': '171.38.34.108:8123', 'user_pass': ''},
#     {'ip_port': '223.241.118.235:8010', 'user_pass': ''},
#     {'ip_port': '171.38.4.176:8123', 'user_pass': ''},
# ]
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
