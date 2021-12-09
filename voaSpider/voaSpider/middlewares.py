class ProxyMiddleware(object):
    def process_request(self, request, spider):

        if request.url.startswith("http://"):
            request.meta['proxy'] = "http://127.0.0.1:" + spider.dbInfo['port']  # http代理
        elif request.url.startswith("https://"):
            request.meta['proxy'] = "https://127.0.0.1:" + spider.dbInfo['port']  # https代理
