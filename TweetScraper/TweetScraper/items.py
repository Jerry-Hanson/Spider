from scrapy import Item, Field


class Tweet(Item):
    tweet_ID = Field()
    tweet = Field()

class User(Item):
    user_ID = Field()
    user = Field()

class Detail(Item):
    tweet_ID = Field()
    detail=Field()


