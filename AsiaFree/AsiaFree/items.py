# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AsiafreeItem(scrapy.Item):
    # define the fields for your item here like:
    article_title = scrapy.Field()
    publish_date = scrapy.Field()
    article_content = scrapy.Field()
