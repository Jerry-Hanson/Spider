from TweetScraper.spiders.TweetCrawler import TweetScraper
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


def start_crawl(*args):
    import os
    base_path = os.getcwd()
    os.chdir(base_path + '/TweetScraper/TweetScraper')
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    keyword, date, Q, dbInfo = args
    query = keyword+" "+"since:"+date
    process.crawl(TweetScraper, query=query, Q=Q, dbInfo=dbInfo)
    process.start()
    os.chdir(base_path)
