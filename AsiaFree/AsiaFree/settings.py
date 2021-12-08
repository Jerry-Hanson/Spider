BOT_NAME = 'AsiaFree'
SPIDER_MODULES = ['AsiaFree.spiders']
NEWSPIDER_MODULE = 'AsiaFree.spiders'
LOG_ENABLED = True
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 0.25

DEFAULT_REQUEST_HEADERS = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko)"
}

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'AsiaFree.middlewares.ProxyMiddleware': 543
}

ITEM_PIPELINES = {
    # 'AsiaFree.pipelines.asiaFreeMongoPipline': 300,
}

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'asiafree'
