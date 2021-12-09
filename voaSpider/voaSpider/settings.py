BOT_NAME = 'voaSpider'
SPIDER_MODULES = ['voaSpider.spiders']
NEWSPIDER_MODULE = 'voaSpider.spiders'
DOWNLOAD_DELAY = 0.25
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
   'voaSpider.middlewares.ProxyMiddleware': 543
}

ITEM_PIPELINES = {
     # 'voaSpider.pipelines.VOAMongoPipline': 100,
}
