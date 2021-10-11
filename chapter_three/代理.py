# https://www.zdaye.com/
# 原理. 通过第三方的机器去发送请求
import requests
import urllib3
urllib3.disable_warnings()  # 这个添加在requests.get('https://xxx.com', verify=False) 上面也有用
# 58.209.234.8:3389
proxies = {
    "https": "https://116.242.92.43:8080"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
resp = requests.get("https://www.baidu.com", headers=headers, proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
