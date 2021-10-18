import requests
import re
import random


def write_mysql(data):
    pass


def get_data(content):
    # 得到数据
    # <a href="http://www.b520.cc/2_2157/">太古神王</a>/净无痕
    results = re.match(r'<a\shref="(.*?)">(.*?)</a>/(.*?)', content, re.S)
    print("书名：" + results.group(2) + " 作者：" + results.group(3) + " 链接：" + results.group(1))
    pass


def parse_ul(html):
    # 处理ul，得到<li>数据
    results = re.findall(r'<li>(.*?)</li>', html, re.S)
    for result in results:
        get_data(result)
    pass


def get_part_html(html):
    result = re.search(r'<div\sclass="novelslist">.*<div\sclass="clear"></div>', html, re.S).group()
    # 得到大分类
    title_results = re.findall(r'<h2>(.*?)</h2>', result, re.S)
    print(title_results)

    # 处理小分类
    # ul拿出来了
    results = re.findall(r'<ul>.*?</ul>', result, re.S)

    for i in range(0, len(results) - 2):
        # 打印大分类
        print(title_results[i])
        # 处理ul，获取小分类
        parse_ul(results[i])
        print("*" * 20)
    pass


def spider(headers, proxies):
    url = "http://www.b520.cc/"
    html = requests.get(url, headers=headers, proxies=proxies).text
    # print(html)
    get_part_html(html)
    pass


if __name__ == "__main__":
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
        'User-Agent': random.choice(user_agent)
    }
    proxies = {"http": None, "https": None}
    spider(headers, proxies)
