import scrapy
from scrapy.settings import Settings
import time
import random
import logging
from ConfigReader import ConfigReader
from items import ScrapydemoItem
from middlewares import ScrapydemoDownloaderMiddleware
from pipelines import ScrapydemoPipeline
from scrapy.crawler import CrawlerProcess

rand_time = [0.1, 0.2, 0.5, 0.3]

# values = {
#         "DOWNLOADER_MIDDLEWARES": {
#             ScrapydemoDownloaderMiddleware : 543
#         },
#         # "LOG_FILE" : "./log/{}.log".format(time.time()),
#         # "LOG_STDOUT" : True,  # 将log重定向到文件中
#         "ITEM_PIPELINES" : {
#             ScrapydemoPipeline : 300
#         },
#         "LOG_LEVEL": "INFO",
#         "CONCURRENT_REQUESTS" : 16  # 这个设置并发数，但是效果好像不是很明显
# }
config = ConfigReader('config/settings.yaml',
                      ["DOWNLOADER_MIDDLEWARES", "ITEM_PIPELINES"]).get_item()
settings = Settings(config)


class MainSpider(scrapy.Spider):
    name = 'main'

    start_urls = ['https://www.epochtimes.com/gb/nsc413.htm']  # 从大陆新闻开始
    base_url = 'https://www.epochtimes.com/gb/nsc413_{0}.htm'
    cur_page = 1  # 记录当前爬到多少页
    logger = logging.getLogger('MainSpiderLogger')

    # 默认相应回调函数
    def parse(self, response):
        """解析起始页"""
        # 获取最多能爬取的页数
        self.max_page = int(response.xpath('//*[@id="main"]/div/div[2]/div[2]/div[31]/a')[-2].xpath('./text()')
                            .extract_first().replace(",", ''))

        # log
        self.logger.info("最大能爬取到%d页", self.max_page)

        yield scrapy.Request(url=self.start_urls[0],
                             callback=self.ParseMain)

    def ParseMain(self, response):
        # 解析起始页
        div_list = response.xpath('//*[@id="main"]/div/div[2]/div[2]/div')

        for div in div_list:
            # title
            title = div.xpath('./div[@class="text"]/div[@class="title"]/a/text()').extract_first()

            if title is not None:
                # log
                self.logger.info('正在解析:' + title)

                # detail_url
                detail_url = div.xpath('./div[@class="text"]/div[@class="title"]/a/@href').extract_first()

                # sleep for some time
                time.sleep(random.choice(rand_time))

                # save data into object
                item = ScrapydemoItem()

                item['title'] = title

                # crawl detail page
                yield scrapy.Request(url=detail_url,
                                     callback=self.ParseDetail,
                                     meta={"item": item})
        # log
        self.logger.info("第%d爬取完毕", self.cur_page)
        self.cur_page += 1

        if self.cur_page > self.max_page:
            self.logger.error("已经爬到最大页数")
            exit(-1)

        yield scrapy.Request(url=self.base_url.format(self.cur_page),
                             callback=self.ParseMain)

    def ParseDetail(self, response):
        release_time = response.xpath('//div[@class="info"]/time/@datetime').extract_first()
        label_list = '|'.join(response.xpath('//a[@rel="tag"]/text()').extract())
        hotness = response.xpath('//span[@class="pageview"]/text()').extract_first()
        article = ''.join(response.xpath('//div[@id="artbody"]//text()').extract()).strip()

        item = response.meta['item']
        item['release_time'] = release_time
        item['labels'] = label_list
        item['hotness'] = hotness
        item['article'] = article

        yield item


if __name__ == "__main__":
    runner = CrawlerProcess(settings)
    runner.crawl(MainSpider)
    runner.start()
