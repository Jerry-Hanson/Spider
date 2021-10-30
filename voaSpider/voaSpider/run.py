from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from voaSpider.spiders.voac_cn import voac_cn
from voaSpider.spiders.voal_ac import voal_ac
from voaSpider.spiders.voal_c import voal_c
from voaSpider.spiders.voal_ga import voal_ga
from voaSpider.spiders.voal_t import voal_t
from voaSpider.spiders.voas_fcn import voas_fcn
from voaSpider.spiders.voas_fg import voas_fg

runner = CrawlerProcess(get_project_settings())

print('''
        1.美国之音美中关系
        2.美国之音中国
        3.美国之音港澳
        4.美国之音台湾
        5.美国之音关键词“中国”
        6.美国之音关键词“反共言论”
        7.美国之音关键词“反中国言论”
        ''')
tem = int(input("请输入需要爬取的网站："))
if tem == 1:
    runner.crawl(voal_ac,name='voal_ac')
elif tem == 2:
    runner.crawl(voal_c, name='voal_c')
elif tem == 3:
    runner.crawl(voal_ga, name='voal_ga')
elif tem == 4:
    runner.crawl(voal_t, name='voal_t')
elif tem == 5:
    runner.crawl(voac_cn, name='voac_cn')
elif tem == 6:
    runner.crawl(voas_fg, name='voas_fg')
elif tem == 7:
    runner.crawl(voas_fcn, name='voas_fcn')
else:
    pass
runner.start()