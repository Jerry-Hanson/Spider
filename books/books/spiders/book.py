# -*- coding: utf-8 -*-
import scrapy
from books.items import BooksItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/']
    Q = None

    def start_requests(self):
        self.Q.put('开始爬取')
        for page_num in range(1, 51):
            url = 'http://books.toscrape.com/catalogue/page-%d.html' % page_num
            yield scrapy.Request(url)

    def parse(self, response):
        for book in response.xpath('//article[@class="product_pod"]'):
            # 初始化Item
            items = BooksItem()

            # 书本标题
            items['title'] = book.xpath('./h3/a/@title').extract_first()

            # 书本价格
            items['price'] = book.xpath('./div/p[@class="price_color"]/text()').extract_first()

            # 书本评级
            review = book.xpath('./p[1]/@class').extract_first()
            items['review'] = review.split(' ')[-1]

            self.Q.put(f"{items['title']}\n{items['price']}\n{items['review']}\n")
            yield items

    def close(spider, reason):
            spider.Q.put('爬取结束')