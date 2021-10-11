# 爬虫：通过编写程序来获取到互联网上的资源
# 需求：用程序模拟浏览器，输入一个网址。从该网址中获取到资源或者内容。

from urllib.request import urlopen
url = "http://www.baidu.com"
response = urlopen(url)
data = response.read().decode('utf-8')  # 读取到网页的页面源代码

with open('My_first_spider.html', mode='w', encoding='utf-8') as f:
    f.write(data)
print("Over!")




