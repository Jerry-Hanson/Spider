import scrapy

from ..items import VoaspiderItem

class voal_ac(scrapy.Spider):
    name = 'voal_ac'
    allowed_domains = ['www.voachinese.com/']
    #美中 https://www.voachinese.com/z/1776?p={}
    start_urls = ['https://www.voachinese.com/z/1776?p={}'.format(i) for i in range(100)]

    def parse(self, response):
        lis = response.xpath("//li[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 fui-grid__inner']")
        for li in lis:
            title = li.xpath("./div/div/a/h4/@title").extract_first()
            if title:
                item = {}
                item['title'] = title
                date = li.xpath("./div/div/span/text()").extract_first()
                item['date'] = date
                href = li.xpath("./div/div/a/@href").extract_first()
                href = "https://www.voachinese.com"+href
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

