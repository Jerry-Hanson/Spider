from AsiaFree.spiders.rfa import RfaSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

settings = get_project_settings()


def start_crawl(*args):
    import os
    base_path = os.getcwd()
    os.chdir(base_path + "/AsiaFree/AsiaFree")  # 切换scrapy运行的当前目录， 用于读取配置文件
    year, month, Q = args
    runner = CrawlerProcess(get_project_settings())
    runner.crawl(RfaSpider, year=year, month=month, Q=Q)
    runner.start()

    os.chdir(base_path)


if __name__ == "__main__":
    start_crawl()
