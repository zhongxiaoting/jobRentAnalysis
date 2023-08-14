# Scrapy settings for JobRent project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobRentAnalysis.settings'    # 项目名.settings

django.setup()

BOT_NAME = "JobRent"

SPIDER_MODULES = ["JobRent.spiders"]
NEWSPIDER_MODULE = "JobRent.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6",
#     "Cache-Control": "max-age=0",
#     "Connection": "keep-alive",
#     "Cookie": "lastCity=101280600; wd_guid=7d235045-cf51-4ea5-8e96-58a029a2b41d; historyState=state; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=1d3cd17b-1cce-43e5-b178-c7e5313dc689; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1682254146; __l=r=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.060000jYAOcGJIMt0_LP8fLMmvsNTM_KITVzq2NM5sNMgOvBKrm6s6i0p6eH5cGXiol9UCRd0xJbBT4p77zCO619eoYgFrb25bAJyi7nTPEjkQFUH09ZM11Xn7YnTrPyvRpNaan5CuyIVj619Wo2Cqnqgn9zxOefJkrDVeHCgeu6EdJuCMRm2YdcVXUjiyOVcgBG6xFtBuO_EHZfoLzaUPD44C_a.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1TsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujdBULP10ZFWIWYs0ZNzU7qGujYkPHfYrHRLnH6d0Addgv-b5HDdnWnvPjDz0AdxpyfqnHcknHbdP160UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dcHbD0TA-b5Hf0mv-b5Hb10APzm1YdnW61Ps%26dt%3D1682254144%26wd%3Dboss%26tpl%3Dtpl_12826_31784_0%26l%3D1544957185%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258ABOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25258C&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%26city%3D101280600%26position%3D100101&s=3&g=%2Fwww.zhipin.com%2Fshenzhen%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; _bl_uid=30lg7g6ktI1eF8oqdoa7mF050FLz; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1682254274; __c=1682254146; __a=84819512.1663338899.1667308956.1682254146.12.3.6.6; __zp_stoken__=230eeJFtLAxwiY3JtJ20xW3h2cHFLeyI3JkhgHGVMWHBKGkE6VEgDIjsIf3NuU3llBV1WODpqcEgxBj4mcXF9Qnk7SVU8Y1JGCGI9aVQCPEo%2FOhJQYnFpbEh8bxNQcgMuR2RkQ0dsBT94XSU%3D",
#     'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "Windows",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": 1
# }

# 设置MySql数据库
# DB_SETTINGS = {
#     'db1': {
#         'host': '127.0.0.1',
#         'db': 'ancient_poetry',
#         'user': 'root',
#         'password': 'root',
#         'port': 3306,
#         'cursorclass': pymysql.cursors.DictCursor,  # 指定cursor类型,
#     },
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "JobRent.middlewares.JobrentSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "JobRent.middlewares.JobrentDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "JobRent.pipelines.JobrentPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

LOG_LEVEL='WARNING'



