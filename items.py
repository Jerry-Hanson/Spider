# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 文章题目
    title = scrapy.Field()
    # 文章人气
    hotness = scrapy.Field()
    # 文章更新时间
    release_time = scrapy.Field()
    # 文章正文
    article = scrapy.Field()
    # 文章标签
    labels = scrapy.Field()
    # 评论
    comments = scrapy.Field()
