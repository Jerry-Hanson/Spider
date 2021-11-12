from BigdataSpider.spiders.mainspider import MainSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def start_crawl(*args):
    """
    start a MainSpider Process
    :param kargs:
    :return
    """
    import os
    base_path = os.getcwd()
    os.chdir(base_path + "/BigdataSpider/BigdataSpider")  # 切换scrapy运行的当前目录， 用于读取配置文件

    settings = get_project_settings()

    finished_page, finished_time,Q = args

    process = CrawlerProcess(settings)
    process.crawl(MainSpider,Q=Q,finished_page=finished_page, finished_time=finished_time)
    process.start()

    os.chdir(base_path)


if __name__ == "__main__":
    start_crawl()
