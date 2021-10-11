from lxml import etree
import requests
from lxml import etree


def spider(url, headers, proxies):
    response = requests.get(url, headers=headers, proxies=proxies).text
    content = etree.HTML(response)
    urls = content.xpath('//*[@id="videoApp"]/div/section[1]/div/ul/li')
    for li in urls:
        url = li.xpath('./a/@href')[0]
        print(url)
        "https://tv.cctv.com/2015/08/27/VIDE1440638136134698.shtml?srcfrom=sogou_vm"
        "/play?query=%C1%C1%BD%A3%201%20site%3Acntv.cn&key=teleplay_2182&j=1&st=6&tvsite=cntv.cn"


def main():
    url = 'https://waptv.sogou.com/teleplay/orswyzlqnrqxsxzsge4decobyg62g.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        # 防盗链：溯源，当前本次请求的上一级是谁
        "Referer": "https://pearvideo.com/video_1743369"
    }
    proxies = {"http": None, "https": None}
    spider(url, headers, proxies)


if __name__ == "__main__":
    main()
