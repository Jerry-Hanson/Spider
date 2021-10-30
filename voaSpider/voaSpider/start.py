from voaSpider.spiders.voac_cn import voac_cn
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import os

def start_crawl():
    base_path = os.getcwd()
    os.chdir(base_path + "/voaSpider/voaSpider")

    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(voac_cn)
    process.start()

    os.chdir(base_path)
