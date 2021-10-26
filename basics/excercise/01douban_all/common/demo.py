import re
from urllib.parse import quote
import requests
from lxml import etree
import random
import csv
import json


class Spider:
    user_agent = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    headers = {
        "User-Agent": random.choice(user_agent),
        "Referer": "https://dushu.baidu.com/pc/reader?gid=4306063500&cid=11348571"
    }
    proxies = {"http": None, "https": None}

    def __init__(self, url):
        self.url = url
        self.big_category_name = None

    def get_html(self, query):
        return requests.get(url=self.url, headers=self.headers, params=query, proxies=self.proxies).text

    def get_href(self):
        query = None
        html = etree.HTML(self.get_html(query))
        big_categories = html.xpath('//div[@class="article"]/div/div')
        # print(big_categories)
        for big_category in big_categories:
            self.big_category_name = big_category.xpath('./a/@name')
            print(self.big_category_name[0].center(40, "="))
            middle_category_hrefs = big_category.xpath('./table/tbody/tr')
            for small_category_hrefs in middle_category_hrefs:
                for href in small_category_hrefs.xpath('./td/a/@href'):
                    self.parse_href(href)

    def parse_href(self, href):
        # full_url = "https://book.douban.com" + quote(href)
        self.url = href

        i = 48
        while True:
            query = {
                "start": i * 20,
                "type": "T"
            }
            if self.get_html(query) is []:
                break
            print("获取第%s页".center(60, "=") % (i))
            html = etree.HTML(self.get_html(query))
            book_name = html.xpath('//div[@id="subject_list"]/ul/li/div[@class="info"]/h2/a/text()')
            print(book_name)
            i = i + 1


def spider():
    url = "https://book.douban.com/tag/"
    main_obj = Spider(url)
    # main_obj.get_href()
    # 测试获取单个页面代码
    href = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4"
    main_obj.parse_href(href)


if __name__ == "__main__":
    spider()
