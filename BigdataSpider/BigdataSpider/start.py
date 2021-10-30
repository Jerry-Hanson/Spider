from BigdataSpider.spiders.mainspider import MainSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def start_crawl(**kargs):
    """
    start a MainSpider Process
    :param kargs:
    :return: process
    """
    import os
    base_path = os.getcwd()
    os.chdir(base_path + "/BigdataSpider/BigdataSpider")  # 切换scrapy运行的当前目录， 用于读取配置文件

    settings = get_project_settings()

    process = CrawlerProcess(settings)
    process.crawl(MainSpider)
    process.start()

    os.chdir(base_path)

if __name__ == "__main__":
    start_crawl()
