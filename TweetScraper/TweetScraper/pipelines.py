import os, logging, json
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User, Detail
from TweetScraper.utils import mkdirs
import pymysql
from pymongo import MongoClient

logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()


class SaveToFilePipeline(object):
    ''' pipeline that save data to disk '''

    def __init__(self):
        self.saveTweetPath = SETTINGS['SAVE_TWEET_PATH']
        self.saveUserPath = SETTINGS['SAVE_USER_PATH']
        self.saveDetailPath = SETTINGS['SAVE_DETAIL_PATH']
        mkdirs(self.saveTweetPath)  # ensure the path exists
        mkdirs(self.saveUserPath)
        mkdirs(self.saveDetailPath)

    def process_item(self, item, spider):
        if isinstance(item, Tweet):
            savePath = os.path.join(self.saveTweetPath, item['id_'])
            if os.path.isfile(savePath):
                pass  # simply skip existing items
                # logger.debug("skip tweet:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update tweet:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add tweet:%s" % item['id_'])

        elif isinstance(item, User):
            savePath = os.path.join(self.saveUserPath, item['id_'])
            if os.path.isfile(savePath):
                pass  # simply skip existing items
                # logger.debug("skip user:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update user:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add user:%s" % item['id_'])
        elif isinstance(item, Detail):
            savePath = os.path.join(self.saveDetailPath, item['id_'])
            if os.path.isfile(savePath):
                pass  # simply skip existing items
                # logger.debug("skip user:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update user:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
        else:
            logger.info("Item type is not recognized! type = %s" % type(item))

    def save_to_file(self, item, fname):
        ''' input: 
                item - a dict like object
                fname - where to save
        '''
        with open(fname + ".json", 'a', encoding='utf-8') as f:
            json.dump(dict(item), f, ensure_ascii=False)


class SavetoMySQLPipeline(object):
    ''' pipeline that save data to mysql '''

    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'asiafree')
        host = spider.settings.get('MYSQL_HOST', 'rm-bp11y14h957ks16573o.mysql.rds.aliyuncs.com')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'Root_123456')
        # 第二步是引入连接数据库，pymysql.connect过程中传入多个参数：数据库主机名（默认为本地主机），数据库登录名（默认为当前用户），数据库密码（默认为空），要打开的数据库名称（无默认，可缺省），MySQL使用的TCP端口（默认为3306，可缺省），数据库字符编码（可缺省），self后边的连接名称可以自取名
        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd)
        # 第三步 获取游标self.连接名.cursor()，游标就像是鼠标一样，后续操作数据库全部靠游标，使用游标的execute命令来执行。
        self.db_cur = self.db_conn.cursor()
        # self.article_content=""

    def close_spider(self, spider):

        # 第六步 关闭数据库
        self.db_conn.close()

    def process_item(self, item, spider):
        # 数据库名：twitter
        # 表1名：tweet 字段：userid,text,datetime
        # 表2名：user 字段：name,screenname,description,createdtime,userid

        if isinstance(item, Tweet):
            text = item['raw_data']
            # userid = row_data['user_id_str']
            # datetime = row_data['created_at']
            # url = row_data['entities']['media']
            # print(url)
            # sql语句
            sql = "INSERT INTO tweet (text) VALUES(%s)"
            # values = (userid,text,datetime)
            values = text
            # print(values)
            # 第四步 用游标执行数据库命令
            self.db_cur.execute(sql, values)
            # 第五步 提交数据库执行
            self.db_conn.commit()

        if isinstance(item, Detail):
            text = item['raw_data']

            sql = "INSERT INTO tweet (text) VALUES(%s)"
            values = text
            self.db_cur.execute(sql, values)
            self.db_conn.commit()

        # elif isinstance(item, User):
        #     row_data = item['raw_data']
        #     name = row_data['name']
        #     screenname = row_data['screen_name']
        #     description = row_data['description']
        #     createdtime = row_data['created_at']
        #     userid = row_data['id_str']
        #     # sql语句
        #     sql = "INSERT INTO user (name,screenname,description,createdtime,userid) VALUES(%s,%s,%s,%s,%s)"
        #     values = (name, screenname, description, createdtime,userid)
        #     # print(values)
        #     # 第四步 用游标执行数据库命令
        #     self.db_cur.execute(sql, values)
        #     # 第五步 提交数据库执行
        #     self.db_conn.commit()
        #     print("successs2")


class SavetoMongoPipeline(object):
    def open_spider(self, spider):
        """
        该方法用于连接数据库
        """
        db_url = spider.settings.get('MONGODB_URI', 'mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME', 'scrapy_default')

        self.db_client = MongoClient('mongodb://localhost:27017')
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
        if isinstance(item, Tweet):
            data = dict(item)
            self.db.tweet.insert_one(data)  # 向集合books中插入数据
        if isinstance(item, User):
            data = dict(item)
            self.db.user.insert_one(data)
        if isinstance(item, Detail):
            tweet_ID = item['tweet_ID']
            tweet_detail = item['detail']
            self.db.tweet.update({"tweet_ID": tweet_ID}, {'$push': {"tweet.tweet_detail": tweet_detail}})
            data = dict(item)
            self.db.detail.insert_one(data)
