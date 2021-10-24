import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from AsiaFree.items import AsiafreeItem


class RfaSpider(scrapy.Spider):
    name = 'rfa'
    allowed_domains = ['www.rfa.org']
    # url_list=[]
    # url_model='https://www.rfa.org/mandarin/story_archive?year={0}&month={1}&b_start:int={2}'
    start_urls = ['https://www.rfa.org/mandarin/story_archive?year=2021&month=2&b_start:int={0}'.format(i) for i in
                  range(0, 1, 1)]

    def parse(self, response):
        article_url_lists = response.xpath("//div[@class='sectionteaser archive']/h2/a/@href").extract()

        for article in article_url_lists:
            yield scrapy.Request(url=article, callback=self.parse_detail)

    def parse_detail(self, response):
        item = AsiafreeItem()
        item['article_title'] = response.xpath(
            "//div[@id='storycontent']/div[@id='storypagemaincol']/div[@class='mobilecontainer']/h1/text()").extract_first()
        print(item['article_title'])
        item['publish_date'] = response.xpath("//div[@id='storytop']/div[@id='dateline']/span[@id='story_date']/text()").extract_first()
        item['article_content'] = response.xpath("//div[@id='storytext']/p/text()").extract()
        yield item

if __name__ == "__main__":
    runner = CrawlerProcess(get_project_settings())
    runner.crawl(RfaSpider)
    runner.start()