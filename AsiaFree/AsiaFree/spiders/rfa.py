import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from AsiaFree.items import AsiafreeItem


class RfaSpider(scrapy.Spider):
    name = 'rfa'
    allowed_domains = ['www.rfa.org']

    # url_list=[]
    # url_model='https://www.rfa.org/mandarin/story_archive?year={0}&month={1}&b_start:int={2}'

    def __init__(self, year=None, month=None, page=0, Q=None, dbInfo=None):
        super(RfaSpider, self).__init__()
        self.Q = Q
        self.year = year
        self.month = month
        self.max_page = 0
        self.page = int(page)
        self.dbInfo = dbInfo
        self.start_url = None

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(RfaSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.Q.put("爬虫结束")

    def start_requests(self):
        if self.page == 0:
            self.start_url = 'https://www.rfa.org/mandarin/story_archive?year={0}&month={1}'.format(self.year,
                                                                                                    self.month)
        elif self.page != 0:
            self.start_url = 'https://www.rfa.org/mandarin/story_archive?b_start:int=0'
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        self.Q.put("开始爬取")
        if self.page == 0:
            self.max_page = int(response.xpath("//ul/li[@class='last']/a/text()").extract_first())
            self.Q.put("预计爬取{0}条文章".format((self.max_page - 1) * 15))
            # print("预计爬取{0}条文章".format((self.max_page-1)*15))
            for index in range(0, (self.max_page - 1) * 15 + 1):
                url = f'https://www.rfa.org/mandarin/story_archive?year={self.year}&month={self.month}&b_start:int={index} '
                yield scrapy.Request(url=url, callback=self.parse_page)
        else:
            self.Q.put("预计爬取{0}条文章".format((self.page - 1) * 15))
            for index in range(0, (self.page - 1) * 15 + 1):
                url = f"https://www.rfa.org/mandarin/story_archive?b_start:int={index}"
                yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        article_url_lists = response.xpath("//div[@class='sectionteaser archive']/h2/a/@href").extract()

        for article in article_url_lists:
            yield scrapy.Request(url=article, callback=self.parse_detail)

    def parse_detail(self, response):
        item = AsiafreeItem()
        item['article_title'] = response.xpath(
            "//div[@id='storycontent']/div[@id='storypagemaincol']/div[@class='mobilecontainer']/h1/text()").extract_first()
        self.Q.put(item['article_title'])
        # print(item['article_title'])
        item['publish_date'] = response.xpath(
            "//div[@id='storytop']/div[@id='dateline']/span[@id='story_date']/text()").extract_first()
        item['article_content'] = response.xpath("//div[@id='storytext']/p/text()").extract()
        yield item


if __name__ == "__main__":
    runner = CrawlerProcess(get_project_settings())
    runner.crawl(RfaSpider)
    runner.start()
