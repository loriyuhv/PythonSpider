# 1. 如何提取单个页面的数据
# 2. 上线程池，多个页面同时抓取
import json
import requests
import random
from concurrent.futures import ThreadPoolExecutor


def download_json(text, page):
    with open("data1.json", "a", encoding='utf8') as f:
        f.write(text + "\n")
    pass


def download_one_page(url, page):
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
    data = {
        "limit": "20",
        "current": page,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": ""
    }
    # 拿到页面源代码
    resp = requests.post(url, headers=headers, proxies=proxies, data=data).json()
    results = resp.get('list')

    # 把数据存放文件
    for result in results:
        download_json(json.dumps(result, ensure_ascii=False), page)

    pass


if __name__ == "__main__":
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    with ThreadPoolExecutor(50) as t:
        for page in range(1, 19133):
            print(page)
            t.submit(download_one_page, url, page)
    print("全部下载完毕！")


# 注意：xpath扩展
# 需求：剔除第一条
# table.xpath('./tr[position()>1]")
# 对数据做简单的处理：\\ /去掉
# txt = (item.replace("\\", "").replace("/", "") for item in txt) # 注意：这个是生成器
# pirnt(list(txt))

