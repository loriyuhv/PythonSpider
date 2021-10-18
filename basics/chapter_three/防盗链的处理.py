import random
import requests

# 1. 拿到contID
url = "https://pearvideo.com/video_1731796"
contId = url.split("_")[1]
print(contId)
mrd = random.random()  # mrd就是个随机小数
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
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)
# https://video.pearvideo.com/mp4/adshort/20211009/cont-1743369-15779562_adpkg-ad_hd.mp4

# 3. srcURL里面的内容进行修整
with open("c.mp4", mode='wb') as f:
    f.write(requests.get(srcUrl, headers=headers, proxies=proxies).content)
print("Over")
# 4. 下载视频
"""
https://pearvideo.com/video_1733844
https://pearvideo.com/video_1731796
https://pearvideo.com/video_1733841

"""



