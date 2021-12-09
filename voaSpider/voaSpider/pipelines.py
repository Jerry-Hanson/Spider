import pymysql
from pymongo import MongoClient


class VoaspiderPipeline(object):
    def __init__(self):
        # connection database
        self.connect = pymysql.connect(host='127.0.0.1', user='root', passwd='liujiahao',
                                       db='voa')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
        # get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")


    def process_item(self, item, spider):
        # sql语句
        dbName = spider.name
        insert_sql = """
        insert into {table} (title,writer,date,href,message) VALUES (%s,%s,%s,%s,%s)
        """
        insert_sql = insert_sql.format(table=dbName)
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['title'], item['writer'],  item['date'], item['href'], item['message']))
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
        print('存储成功')

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()



class VOAMongoPipline:
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