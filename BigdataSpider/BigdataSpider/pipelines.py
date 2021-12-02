# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class BigdataspiderPipeline:
    # def __init__(self):
    #     # self.mongodb_url = settings['MONGODB_URI']
    #     # self.mongodb_db_name = settings['MONGODB_DB_NAME']
    #     #
    #     # self.client = MongoClient(self.mongodb_url)
    #     # self.db = self.client[self.mongodb_db_name]

    def open_spider(self, spider):
        self.dbInfo = spider.dbInfo
        self.client = MongoClient(self.dbInfo['dbIp'])
        self.db = self.client[self.dbInfo['dbName']]


    # def __del__(self):
    #     self.client.close()

    def process_item(self, item, spider):
        self.db.Bigdata.insert_one(dict(item))
        return item
