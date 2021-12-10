import re, json, logging
from urllib.parse import quote
import copy
from scrapy import http, signals
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider
from scrapy.core.downloader.middleware import DownloaderMiddlewareManager
from scrapy.utils.project import get_project_settings
from scrapy_selenium import SeleniumRequest, SeleniumMiddleware
from TweetScraper.items import Tweet, User, Detail


class TweetScraper(CrawlSpider):
    name = 'TweetScraper'
    allowed_domains = ['twitter.com']

    def __init__(self, query='中共', dbInfo=None, Q=None):
        self.url = (
            f'https://api.twitter.com/2/search/adaptive.json?'
            f'include_profile_interstitial_type=1'
            f'&include_blocking=1'
            f'&include_blocked_by=1'
            f'&include_followed_by=1'
            f'&include_want_retweets=1'
            f'&include_mute_edge=1'
            f'&include_can_dm=1'
            f'&include_can_media_tag=1'
            f'&skip_status=1'
            f'&cards_platform=Web-12'
            f'&include_cards=1'
            f'&include_ext_alt_text=true'
            f'&include_quote_count=true'
            f'&include_reply_count=1'
            f'&tweet_mode=extended'
            f'&include_entities=true'
            f'&include_user_entities=true'
            f'&include_ext_media_color=true'
            f'&include_ext_media_availability=true'
            f'&send_error_codes=true'
            f'&simple_quoted_tweet=true'
            f'&query_source=typed_query'
            f'&pc=1'
            f'&spelling_corrections=1'
            f'&ext=mediaStats%2ChighlightedLabel'
            f'&count=20'
            f'&tweet_search_mode=live'
        )
        self.url = self.url + '&q={query}'
        self.query = query
        self.num_search_issued = 0
        # regex for finding next cursor
        self.cursor_re = re.compile('"(scroll:[^"]*)"')
        self.detail_conversation_re = re.compile('conversationthread')
        self.Q = Q
        self.dbInfo = dbInfo
        # 需要定时更新
        self.detail_headers = {
            'authority': 'twitter.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'x-twitter-client-language': 'en',
            'x-csrf-token': '2b137fa72236f217736dcd584d136c38b57f8d3fb6967fecdc4f62f211e5aa6e6a84b8000f4adc8d6a9d327371de44e9b470e3e2abda795ba540af40f26e2dd3cbef878814084fe8cf2e796d8904588c',
            'sec-ch-ua-mobile': '?0',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-active-user': 'yes',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://twitter.com/journny1999/status/1465699820677435399',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'cookie': 'kdt=lj6rABjhNXDpQpHM4V6bcA2RbFguCC15ZPVCy85G; dnt=1; remember_checked_on=1; ads_prefs="HBESAAA="; personalization_id="v1_23hOXYs09HUrlnwcCqfT6Q=="; guest_id=v1%3A162719985151538512; des_opt_in=Y; guest_id_marketing=v1%3A162719985151538512; guest_id_ads=v1%3A162719985151538512; g_state={"i_l":0}; external_referer=padhuUp37zjgzgv1mFWxJ5Xq0CLV%2BbpWuS41v6lN3QU%3D|0|8e8t2xd8A2w%3D; gt=1466269184825106432; at_check=true; mbox=PC#bb5b1775f75f43458aa5aa6810c60e3a.38_0#1701665611|session#c92ae7443db040c0a78c13e44ea30a71#1638422670; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMlIfnl9AToMY3NyZl9p%250AZCIlOGY3NzNlNjJiNWMzNTQ4NjE0ZWZlMTg2MjY4YTFlNGE6B2lkIiUyOTA2%250AZjU1NDk4M2UzZjNkOTM4MWYxN2Q3NGJlNWU1Yw%253D%253D--8a541d83f5ce0358c4d3b494eeea25709ab27eb0; auth_token=3a3579487d12a10f14950aef3fc02f898a3df8e0; ct0=2b137fa72236f217736dcd584d136c38b57f8d3fb6967fecdc4f62f211e5aa6e6a84b8000f4adc8d6a9d327371de44e9b470e3e2abda795ba540af40f26e2dd3cbef878814084fe8cf2e796d8904588c; twid=u%3D1418830181561733121; att=1-q1gpkIza5CT9hP7GNnxntTSNUum8BQzkS6IP1V6z',
        }

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TweetScraper, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.Q.put("爬虫结束")

    def start_requests(self):
        """
        Use the landing page to get cookies first
        """
        yield SeleniumRequest(url="https://twitter.com/explore", callback=self.parse_home_page)

    def parse_home_page(self, response):
        """
        Use the landing page to get cookies first
        """
        # inspect_response(response, self)
        self.update_cookies(response)
        for r in self.start_query_request():
            yield r

    def update_cookies(self, response):
        driver = response.meta['driver']
        try:
            self.cookies = driver.get_cookies()
            self.x_guest_token = driver.get_cookie('gt')['value']
            # self.x_csrf_token = driver.get_cookie('ct0')['value']
        except:
            self.Q.put('cookies are not updated!')

        self.headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-guest-token': self.x_guest_token,
        }

    def start_query_request(self, cursor=None):  # 一开始cursor为空
        """
        Generate the search request
        """

        # 判断有没有cursor
        if cursor:
            url = self.url + '&cursor={cursor}'
            url = url.format(query=quote(self.query), cursor=quote(cursor))
        else:
            url = self.url.format(query=quote(self.query))
        # print(url)
        # print(self.cookies)

        request = http.Request(url, callback=self.parse_result_page, cookies=self.cookies, headers=self.headers)
        yield request

        self.num_search_issued += 1
        # 100次更新一次cookie
        if self.num_search_issued % 100 == 0:
            # get new SeleniumMiddleware
            for m in self.crawler.engine.downloader.middleware.middlewares:
                if isinstance(m, SeleniumMiddleware):
                    m.spider_closed()
            self.crawler.engine.downloader.middleware = DownloaderMiddlewareManager.from_crawler(self.crawler)
            # update cookies
            yield SeleniumRequest(url="https://twitter.com/explore", callback=self.update_cookies, dont_filter=True)

    def detail_query_requests(self, tweetID, cursor=None):
        if cursor != None:
            url = f'https://twitter.com/i/api/graphql/HES7n5js5LRVLpW3Wy8fKQ/TweetDetail?variables=' \
                  f'{{"focalTweetId":"{tweetID}",' \
                  f'"cursor":"{cursor}",' \
                  f'"referrer":"tweet",' \
                  f'"controller_data":"DAACDAAFDAABDAABDAABCgABAAAAAAAAAAgAAAwAAgoAAQAAAAAAAAABCgACZCnMNF4h1ioLAAMAAAAG576O5Zu9AAAAAAA=",' \
                  f'"includePromotedContent":true,' \
                  f'"withHighlightedLabel":true,' \
                  f'"withCommunity":false,' \
                  f'"withTweetQuoteCount":true,' \
                  f'"withBirdwatchNotes":false,' \
                  f'"withBirdwatchPivots":false,' \
                  f'"withTweetResult":true,' \
                  f'"withReactions":false,' \
                  f'"withSuperFollowsTweetFields":false,' \
                  f'"withSuperFollowsUserFields":false,' \
                  f'"withUserResults":false,' \
                  f'"withVoice":true}}'
        else:
            url = f'https://twitter.com/i/api/graphql/HES7n5js5LRVLpW3Wy8fKQ/TweetDetail?variables=' \
                  f'{{"focalTweetId":"{tweetID}",' \
                  f'"referrer":"app",' \
                  f'"controller_data":"DAACDAAFDAABDAABDAABCgABAAAAAAAAAIAAAAwAAgoAAQAAAAAAAAAgCgAChhtX288R0ywLAAMAAAAG5Lit5YWxAAAAAAA=",' \
                  f'"includePromotedContent":true,' \
                  f'"withHighlightedLabel":true,' \
                  f'"withCommunity":false,' \
                  f'"withTweetQuoteCount":true,' \
                  f'"withBirdwatchNotes":false,' \
                  f'"withBirdwatchPivots":false,' \
                  f'"withTweetResult":true,' \
                  f'"withReactions":false,' \
                  f'"withSuperFollowsTweetFields":false,' \
                  f'"withSuperFollowsUserFields":false,' \
                  f'"withUserResults":false,' \
                  f'"withVoice":true}}'
        request = http.Request(url=url, callback=self.parse_detail_page, headers=self.detail_headers,
                               meta={"dont_merge_cookies": True, "tweetID": copy.deepcopy(tweetID)}, dont_filter=True)
        yield request

    def parse_result_page(self, response):
        """
        Get the tweets & users & next request
        """
        # inspect_response(response, self)

        # handle current page
        data = json.loads(response.text)
        for item in self.parse_tweet_item(data['globalObjects']['tweets']):
            yield item
        for item in self.parse_user_item(data['globalObjects']['users']):
            yield item

        # get next page
        cursor = self.cursor_re.search(response.text).group(1)
        for r in self.start_query_request(cursor=cursor):
            yield r

    # TODO parse_detail_page
    def parse_detail_page(self, response):
        tweetID = response.meta['tweetID']
        data = json.loads(response.text)
        entries = data['data']['threaded_conversation_with_injections']['instructions'][0]['entries']
        for item in self.parse_detail_item(items=entries, id=tweetID):
            yield item
        try:
            content = data['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][-1]['content']
        except IndexError as err:
            return
        if ('itemContent' in content):
            itemContent = content['itemContent']
            if ('value' in itemContent):
                for detail_next_request in self.detail_query_requests(tweetID=tweetID, cursor=itemContent['value']):
                    yield detail_next_request
            else:
                pass
        else:
            pass

    def parse_conversition_page(self, response):
        data = json.loads(response.text)
        for item in self.parse_detail_item(data['data']):
            yield item

    def parse_tweet_item(self, items):
        for k, v in items.items():
            # assert k == v['id_str'], (k,v)
            tweet = Tweet()
            tweet['tweet_ID'] = k
            # tweet['raw_data'] = filter_emoji(v['full_text'], '')
            tweet['tweet'] = v
            yield tweet
            for detail_request in self.detail_query_requests(tweetID=k):
                yield detail_request

    def parse_user_item(self, items):
        for k, v in items.items():
            # assert k == v['id_str'], (k,v)
            user = User()
            user['user_ID'] = k
            user['user'] = v
            yield user

    def parse_detail_item(self, items, id):

        for v in items:
            detail = Detail()
            detail['tweet_ID'] = id
            detail['detail'] = v
            yield detail


if __name__ == "__main__":
    runner = CrawlerProcess(get_project_settings())
    runner.crawl(TweetScraper, query='中共')
    runner.start()
