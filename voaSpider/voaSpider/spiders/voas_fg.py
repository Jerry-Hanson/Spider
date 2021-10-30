import scrapy

from ..items import VoaspiderItem

class voas_fg(scrapy.Spider):
    name = 'voas_fg'
    allowed_domains = ['www.voachinese.com/']
    #网站可进行修改，xpath结构相同
    #台湾 https://www.voachinese.com/z/1769?p={}
    #start_urls = ['https://www.voachinese.com/z/1769?p={}'.format(i) for i in range(100)]
    #港澳 https://www.voachinese.com/z/1755?p={}
    #start_urls = ['https://www.voachinese.com/z/1755?p={}'.format(i) for i in range(100)]
    #美中 https://www.voachinese.com/z/1776?p={}
    #start_urls = ['https://www.voachinese.com/z/1776?p={}'.format(i) for i in range(100)]
    #中国 https://www.voachinese.com/z/1757?p={}
    # start_urls = ['https://www.voachinese.com/z/1757?p={}'.format(i) for i in range(100)]
    #关键词 中国 https://www.voachinese.com/s?k=%E4%B8%AD%E5%9B%BD&tab=news&pi={}&r=any&pp=50
    #start_urls = ['https://www.voachinese.com/s?k=%E4%B8%AD%E5%9B%BD&tab=news&pi={}&r=any&pp=50'.format(i) for i in range(100)]
    #关键词 反共言论 https://www.voachinese.com/s?k=%E5%8F%8D%E5%85%B1%E8%A8%80%E8%AE%BA&tab=all&pi={}&r=any&pp=50

    start_urls = ['https://www.voachinese.com/s?k=%E5%8F%8D%E5%85%B1%E8%A8%80%E8%AE%BA&tab=all&pi={}&r=any&pp=50'.format(i) for i in range(100)]


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

