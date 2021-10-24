# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class AsiafreePipeline:
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
        self.article_content=""

    def close_spider(self, spider):
        # 第五步 提交数据库执行
        self.db_conn.commit()
        # 第六步 关闭数据库
        self.db_conn.close()

    def process_item(self, item, spider):
        self.article_content=""
        for article in item['article_content']:
            self.article_content+=article
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            item['article_title'],
            item['publish_date'],
            self.article_content
        )
        sql="INSERT INTO article (article_title,publish_date,article_content) VALUES(%s,%s,%s)"
        # 第四步 用游标执行数据库命令
        self.db_cur.execute(sql, values)

