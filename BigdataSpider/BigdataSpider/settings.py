BOT_NAME = 'BigdataSpider'

SPIDER_MODULES = ['BigdataSpider.spiders']
NEWSPIDER_MODULE = 'BigdataSpider.spiders'

LOG_LEVEL = "INFO"
RANDOMIZE_DOWNLOAD_DELAY = True

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'BigdataSpider.middlewares.ProxyMiddleware': 543,
}

ITEM_PIPELINES = {
    # 'BigdataSpider.pipelines.BigdataspiderPipeline': 300,
}
