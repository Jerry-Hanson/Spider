# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient



class BigdataspiderPipeline:
    def open_spider(self, spider):
        """
        该方法用于连接数据库
        """
        #get(key,default)
        db_url = spider.dbInfo['dbIp']
        db_name = spider.dbInfo['dbName']

        self.db_client = MongoClient(db_url)
        self.db = self.db_client[db_name]

    def close_spider(self, spider):
        """
        该方法用于关闭数据库
        """
        self.db_client.close()

    def process_item(self, item, spider):
        """
        该方法用于插入数据
        """
        self.insert_db(item)

        return item

    def insert_db(self, item):
        data = dict(item)
        self.db.article.insert_one(data)  # 向集合books中插入数据

