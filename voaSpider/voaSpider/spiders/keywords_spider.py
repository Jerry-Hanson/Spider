import scrapy
import urllib

from ..items import VoaspiderItem


class keywords_spider(scrapy.Spider):
    def __init__(self, keyword, dbInfo):
        self.keyword = keyword
        self.dbInfo = dbInfo
        keyword_encode = urllib.parse.quote(self.keyword)
        self.start_urls = ['https://www.voachinese.com/s?k={}&tab=news&pi={}&r=any&pp=50'.format(keyword_encode, i) for
                           i in
                           range(100)]

        super(keywords_spider, self).__init__()

    name = "keyword_spider"
    allowed_domains = ['www.voachinese.com/']

    def parse(self, response):

        lis = response.xpath("//li[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 fui-grid__inner']")
        for li in lis:
            title = li.xpath("./div/div/a/@title").extract_first()
            if title:
                item = {}
                item['title'] = title
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
