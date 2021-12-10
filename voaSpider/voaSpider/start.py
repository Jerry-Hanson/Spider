from voaSpider.spiders.keywords_spider import keywords_spider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import os


def start_crawl(*args):
    keyword, Q, dbInfo = args

    base_path = os.getcwd()
    os.chdir(base_path + "/voaSpider/voaSpider")

    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(keywords_spider, keyword=keyword, Q=Q, dbInfo=dbInfo)
    process.start()

    os.chdir(base_path)
