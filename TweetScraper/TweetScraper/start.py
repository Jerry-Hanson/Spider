from scrapy import cmdline

cmdline.execute("scrapy crawl TweetScraper -a query=\"中共\"".split())