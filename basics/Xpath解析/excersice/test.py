# 利用xpath爬取笔趣阁的小说分类
# 结果：['玄幻小说', '修真小说', '都市小说', '穿越小说', '网游小说', '科幻小说', '最近更新小说列表', '最新入库小说']
import requests
from lxml import etree

url = "http://www.b520.cc/"

headers = {
    "User-Agent": "I wanted to be an engineer."
}
proxies = {'http': None, "https": None}

response = requests.get(url, headers=headers, proxies=proxies).text
# print(response)

html = etree.HTML(response)
title = html.xpath('//*[@id="main"]/div/div/h2/text()')[1:]
print(title)


