import random
from lxml import etree
import requests


def download(name, srcUrl, headers, proxies):

    video_name = name.replace(':' and "?" and "\\" and "/" and "*" and '"' and "'" and "|" and "、", " ") + ".mp4"
    try:
        with open(video_name, mode="wb") as f:
            f.write(requests.get(srcUrl, headers=headers, proxies=proxies).content)
    except FileExistsError:
        print("error")
    print("Over")


def full_spider(name, url):
    contId = url.split("_")[1]
    # print(contId)
    mrd = random.random()   #  mrd就是个随机小数
    videoStatus = f'https://pearvideo.com/videoStatus.jsp?contId={contId}&mrd={mrd}'
    print(videoStatus)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        # 防盗链：溯源，当前本次请求的上一级是谁
        "Referer": f"https://pearvideo.com/video_{contId}"
    }
    proxies = {"http": None, "https": None}
    resp = requests.get(videoStatus, headers=headers, proxies=proxies)


    # 2. 拿到videoStatus返回的json. -> srcURL
    dic = resp.json()
    srcUrl = dic['videoInfo']['videos']['srcUrl']
    # print(srcUrl)
    systemTime = dic['systemTime']

    srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
    print(srcUrl)
    print("="*50)

    # # 3. srcURL里面的内容进行修整
    download(name, srcUrl, headers, proxies)


def parse_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        # 防盗链：溯源，当前本次请求的上一级是谁
        "Referer": "https://pearvideo.com/video_1743369"
    }
    proxies = {"http": None, "https": None}
    response = requests.get(url, headers=headers, proxies=proxies).text
    content = etree.HTML(response)
    li = content.xpath('/html/body/li')
    for i in li:
        link_url = i.xpath('./div/a/@href')[0]
        name = i.xpath('./div/a/div[2]/text()')[0]
        print(name)
        print(type(name))
        full_url = "https://pearvideo.com/" + link_url
        full_spider(name, full_url)


def spider_video_url(page_counts, main_url):
    """
    由于是Ajax的页面渲染，所以需要循环来获取每页的url
    :param page_counts: 页数
    :param main_url: 主页url
    :return: 无
    """
    # mrd是随机小数
    mrd = random.random()
    # 从第3页开始，到用户输入的页数为止
    for i in range(3, int(page_counts)+1):
        number = i * 12
        full_url = main_url + f"start={number}&mrd={mrd}"
        parse_url(full_url)


def main():
    """
    主函数：
    这里主要有两个参数，一个用户输入的
    爬取页数page_counts和已经被给予的main_url参数
    调用spider_video_url函数进行获取详细的视频链接
    """
    # 用户界面
    page_counts = input("请输入爬取页数：")
    # 爬取界面
    main_url = f"https://pearvideo.com/category_loading.jsp?reqType=5&categoryId=5&"
    spider_video_url(page_counts, main_url)


if __name__ == "__main__":
    """
    主函数入口
    """
    main()
