import scrapy
import time
import random
import logging
from BigdataSpider.items import BigdataspiderItem
from datetime import datetime

rand_time = [0.1, 0.2, 0.5, 0.3]


class MainSpider(scrapy.Spider):
    name = 'mainspider'

    start_urls = ['https://www.epochtimes.com/gb/nsc413.htm']  # 从大陆新闻开始
    base_url = 'https://www.epochtimes.com/gb/nsc413_{0}.htm'
    cur_page = 1  # 记录当前爬到多少页
    logger = logging.getLogger('MainSpiderLogger')

    def __init__(self, finished_page = 0, finished_time = None):
        """
        控制爬取页数和时间
        """
        super(MainSpider, self).__init__()
        self.finished_page = finished_page
        self.finished_time = finished_time
        if self.finished_time != None:
            self.finished_time = datetime.strptime(finished_time, "%Y-%m-%d")

        # 控制页数和时间只能二选一
        if self.finished_time != None:
            self.use_page = False
        else:
            self.use_page = True

    def get_maxpage(self):
        return self.max_page

    # 默认相应回调函数
    def parse(self, response):
        """解析起始页"""
        # 获取最多能爬取的页数
        self.max_page = int(response.xpath('//*[@id="main"]/div/div[2]/div[2]/div[31]/a')[-2].xpath('./text()')
                            .extract_first().replace(",", ''))
        if self.finished_page == 0 and self.use_page:
            self.finished_page = self.max_page

        # log
        if self.use_page:
            self.logger.info("最大能爬取到%d页", self.max_page)
            self.logger.info("预计爬取到%d页", self.finished_page)
        else:
            self.logger.info(f"预计爬取到{self.finished_time}为截止日期的文章", )

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
                item = BigdataspiderItem()

                item['title'] = title

                # crawl detail page
                yield scrapy.Request(url=detail_url,
                                     callback=self.ParseDetail,
                                     meta={"item": item})
        # log
        self.logger.info("第%d爬取完毕", self.cur_page)
        self.cur_page += 1

        if self.cur_page > self.max_page:
            self.logger.info('已经爬取到最大页数')
            exit(-1)
        # 控制爬取页数
        if self.cur_page >= self.finished_page and self.use_page:
            self.logger.info('已经爬取到指定的页数')

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

        # 控制爬取时间
        if self.use_page is False and release_time != None:
            cur = datetime.strptime(release_time.split('T')[0], "%Y-%m-%d")
            if cur < self.finished_time:
                self.logger.info("已经爬取到指定的时间")
                # 退出爬虫
                exit(-1)


        yield item