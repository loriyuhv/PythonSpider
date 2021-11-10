import re
from urllib.parse import urlencode

import scrapy
from douban.items import DoubanItem


class DemoSpider(scrapy.Spider):
    name = 'demo'   # 爬虫名
    allowed_domains = ['book.douban.com']   # 允许爬取的范围

    def start_requests(self):
        base_url = 'https://movie.douban.com/top250?'
        pages = 10
        for page in range(0, pages):
            data = {"start": page*25}
            params = urlencode(data)
            full_url = base_url + params
            # print(full_url)
            yield scrapy.Request(full_url, self.parse)

    def parse(self, response, **kwargs):

        lists = response.xpath('//div[@class="article"]/ol[@class="grid_view"]/li')
        item = DoubanItem()
        name = {}
        item["name"] = name
        for li in lists:

            # 用xpath解析，获取电影名称
            # 电影名称
            title = li.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()').extract()
            other = li.xpath('.//div[@class="hd"]/a/span[@class="other"]/text()').extract()
            if title[0] is None:
                item["name"]["title"] = []
            else:
                item["name"]["title"] = [title.strip().strip("/\xa0") for title in title]

            if other[0] is None:
                item["name"]["other"] = []
            else:
                item["name"]["other"] = [title.strip().strip("/\xa0") for title in other]

            information = li.xpath('.//div[@class="bd"]/p[1]').extract_first()
            # print(information)

            # 需要用正则解析的字符串
            """导演: 罗伯·莱纳 Rob Reiner   主演: 玛德琳·卡罗尔 Madeline Carroll / 卡...<br>
                                        2010 / 美国 / 剧情 喜剧 爱情"""

            # 导演
            r = re.compile(r'.*?导演:(.*?)主演:', re.S)
            director = re.search(r, information)
            if director is None:
                director_text = re.search(r'.*?导演:(.*?)\s\s.*?\.\.\.', information, re.S)
                if director_text is None:
                    item["director"] = None
                else:
                    item["director"] = director_text.group(1)
            else:
                item["director"] = director.group(1).strip('\xa0')

            # 演员
            pattern = re.compile(r'.*?主演:(.*?)<br>', re.S)
            actor = re.search(pattern, information)
            if actor is None:
                item["actor"] = None
            else:
                item["actor"] = actor.group(1)

            # 时间
            pattern_time = re.compile(r'.*?<br>.*?(\d+)\s+', re.S)
            time = re.search(pattern_time, information)
            if time is None:
                item["time"] = None
            else:
                item["time"] = time.group(1)

                # 国家
            pattern_nation = re.compile(r'.*?<br>.*?/\s(.*?)\s/', re.S)
            nation = re.search(pattern_nation, information)
            if nation is None:
                item["nation"] = None
            else:
                item["nation"] = nation.group(1)

            # 剧情
            pattern_scenario = re.compile(r'.*?<br>.*?/.*?/(.*?)\s\s', re.S)
            scenario = re.search(pattern_scenario, information)
            if scenario is None:
                item["scenario"] = None
            else:
                item["scenario"] = scenario.group(1).strip('\xa0')

            yield item
