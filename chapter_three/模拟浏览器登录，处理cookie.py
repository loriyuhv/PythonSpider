# 登录 --> 得到cookie
# 带着cookie 去请求网站url --> 网站的内容
# 必须得把上面的两个操作连接起来
# 我们可以使用session进行请求 -> session可以被认为是一连串的请求，在这个过程cookie不会丢失
import requests

# 会话
session = requests.session()

# 1. 登录
url = 'https://passport.17k.com/ck/user/login'
data = {
    "loginName": "18370508206",
    "password": "wsw20010420"
}
response = session.post(url, data)
# print(response.text)
# print(response.cookies)
# 2. 获取数据
# 刚才的那个session中是有cookie的
url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
response_data = session.get(url)
print(response_data.json())
# with open("bookshelf_data.json", mode='w', encoding='utf-8') as f:
#     f.write(str(response_data.json()))
headers = {
    "User-Agent": "",
    "Cookie": ""
}
# resq = requests.get(url, headers=headers)
# print(resq.text)
print("Over!")

