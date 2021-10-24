# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
# settings for spiders
COOKIES_ENABLED = True
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'

# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'
SAVE_DETAIL_PATH = './Data/detail/'

DOWNLOAD_DELAY = 1.0

# settings for selenium
from shutil import which

SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_BROWSER_EXECUTABLE_PATH = which('firefox')
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS = ['-headless']
# SELENIUM_DRIVER_ARGUMENTS=[]
# '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

ITEM_PIPELINES = {
    # 'TweetScraper.pipelines.SaveToFilePipeline':100,
    # 'TweetScraper.pipelines.SavetoMySQLPipeline':100,
    #'TweetScraper.pipelines.SavetoMongoPipeline': 100,
}

SPIDER_MIDDLEWARES = {
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': None
}
# settings for mysql
MYSQL_SERVER = "rm-bp11y14h957ks16573o.mysql.rds.aliyuncs.com"
MYSQL_DB = "asiafree"
MYSQL_TABLE = "tweets"  # the table will be created automatically
MYSQL_USER = "root"  # MySQL user to use (should have INSERT access granted to the Database/Table
MYSQL_PWD = "Root_123456"  # MySQL user's password

# settings for mongodb
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'twitter'
