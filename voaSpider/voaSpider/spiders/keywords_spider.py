import re

import scrapy
import urllib

from scrapy import signals

from ..items import VoaspiderItem


class keywords_spider(scrapy.Spider):
    def __init__(self, keyword, Q, dbInfo):
        self.keyword = keyword
        self.dbInfo = dbInfo
        self.Q = Q
        self.keyword_encode = urllib.parse.quote(self.keyword)
        self.start_urls = [f'https://www.voachinese.com/s?k={self.keyword_encode}&tab=news&pi=1&r=month&pp=50']

        super(keywords_spider, self).__init__()

    name = "keyword_spider"
    allowed_domains = ['www.voachinese.com/']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(keywords_spider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.Q.put("爬虫结束")


    def parse(self, response):
        self.Q.put("开始爬取")
        result = response.xpath("//span[@class='“results-count”']/text()").extract_first()
        result = re.match(r'[1-9]+\.?[0-9]*', result).group()
        self.Q.put("检索到关键词"+result+"个")
        self.max_page = int(result)//50 + 1
        for i in range(1,self.max_page+1):
            url = f'https://www.voachinese.com/s?k={self.keyword_encode}&tab=news&pi={i}&r=month&pp=50'
            yield scrapy.Request(url=url, callback=self.parse_home, dont_filter=True)

    def parse_home(self,response):
        lis = response.xpath("//li[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 fui-grid__inner']")
        for li in lis:
            title = li.xpath("./div/div/a/@title").extract_first()
            if title:
                item = {}
                item['title'] = title
                self.Q.put(title)
                date = li.xpath("./div/div/span/text()").extract_first()
                item['date'] = date
                href = li.xpath("./div/div/a/@href").extract_first()
                href = "https://www.voachinese.com" + href
                item['href'] = href
                yield scrapy.Request(href, callback=self.parse_detail, dont_filter=True, meta={"item": item})

    def parse_detail(self, response):
        item = response.meta["item"]
        writer = response.xpath("//li[@class='links__item']/a/text()").extract_first()
        if writer:
            item['writer'] = writer
        else:
            item['writer'] = '佚名'
        message = response.xpath("//*[@id=\"article-content\"]/div/p/text()").extract()
        if message:
            str1 = ''
            for i in message:
                str1 = str1 + i
            item['message'] = str1
            yield item
