USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
COOKIES_ENABLED = True
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'

SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'
SAVE_DETAIL_PATH = './Data/detail/'
# RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 0.25
MYEXT_ENABLED =True
from shutil import which
import os

SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_BROWSER_EXECUTABLE_PATH = which('firefox')
service_log_path = os.devnull
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS = ['-headless']
# SELENIUM_DRIVER_ARGUMENTS=[]
# '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800,

}

ITEM_PIPELINES = {
    # 'TweetScraper.pipelines.SaveToFilePipeline':100,
    # 'TweetScraper.pipelines.SavetoMySQLPipeline':100,
    # 'TweetScraper.pipelines.SavetoMongoPipeline': 100,
}

EXTENSIONS = {
   'TweetScraper.extensions.LogStats': 1
}

SPIDER_MIDDLEWARES = {
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': None
}
# settings for mysql
MYSQL_SERVER = ""
MYSQL_DB = "asiafree"
MYSQL_TABLE = "tweets"  # the table will be created automatically
MYSQL_USER = "root"  # MySQL user to use (should have INSERT access granted to the Database/Table
MYSQL_PWD = ""  # MySQL user's password