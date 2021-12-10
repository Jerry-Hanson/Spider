BOT_NAME = 'BigdataSpider'

SPIDER_MODULES = ['BigdataSpider.spiders']
NEWSPIDER_MODULE = 'BigdataSpider.spiders'

LOG_LEVEL = "INFO"
DOWNLOAD_DELAY = 0.25

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'BigdataSpider.middlewares.ProxyMiddleware': 543,
}

ITEM_PIPELINES = {
    'BigdataSpider.pipelines.BigdataspiderPipeline': 300,
}

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'bigdate'
