# 主要解决爬取页面为空
import requests
import random
session = requests.session()

url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=7540&type=T"

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
    "Cookie": """ll="118209"; bid=3HJVjrjGdTY; __gads=ID=bdae35907caed1a8-220e4728b3cc003f:
    T=1634805323:RT=1634805323:S=ALNI_MaQtsgLnvy8jYIZSTfOHApimDnfvA; gr_user_id=13451131-
    1f58-4661-a06b-257cb7a5ede7; _pk_ses.100001.3ac3=*; _vwo_uuid_v2=
    D4FC27EA12CEC8F93EC45F9465710AF64|d93f4f2997729f1d02e72bff0f0b4b39; __utma=
    30149280.1862615810.1635144213.1635144213.1635144213.1; __utmz=
    30149280.1635144213.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=
    30149280; __utmc=81379588; __utma=81379588.63383535.1635144213.1635144213.1635144213.1
    ; __utmz=81379588.1635144213.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct=y
    ; __utmt_douban=1; __utmt=1; dbcl2="204299781:UXsox+laRrw"; ck=9jB6; _pk_id.100001.3ac3
    =7a4097b6383b9e72.1635144210.1.1635151798.1635144210.; ap_v=
    0,6.0; __utmb=30149280.38.10.1635144213; __utmb=
    81379588.38.10.1635144213; push_noty_num=0; push_doumail_num=0"""
}
proxies = {"http": None, "https": None}

response = requests.get(url, headers=headers, proxies=proxies).text
print(type(response))
# print(response)
if response is None:
    print("error")
else:
    print("Ok")


