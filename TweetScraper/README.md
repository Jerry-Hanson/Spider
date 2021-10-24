# Introduction #
抓取的包为在https://twitter.com/explore 滚动页面产生的adaptive Json数据包
和在点进推文产生的tweetdetail Json数据包

本爬虫基于 https://github.com/jonbakerfish/TweetScraper 开发

# Installation #
环境需要
1. scrapy
2. selenium 及对应驱动，推荐火狐，chrome也可以，但需要修改相关配置
3. pip 安装 scrapy-selenium
4. 运行时可能会报错的原因有：urllib的版本过高，驱动版本不对应，attr的版本不一致

# Usage #

1. 运行爬虫使用start.py

# storage #

1. 存储位置位于Data目录
2. 目前采用json数据存储
3. 存储格式为json数据包原格式，尚未进行数据清洗






