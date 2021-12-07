import scrapy


class AsiafreeItem(scrapy.Item):
    article_title = scrapy.Field()
    publish_date = scrapy.Field()
    article_content = scrapy.Field()
