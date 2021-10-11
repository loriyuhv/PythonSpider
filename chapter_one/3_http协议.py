# http协议：Hyper Text Transfer Protocol(超文本传输协议）
# HTTP协议把一条消息分为三大块内容，无论是请求还是相应都是三块内容
"""
请求：
    请求行 -->  请求方式(get, post) 请求url地址，协议
    请求头 -->  放一些服务器要使用的附加信息
    请求体 -->  一般放一些请求参数

响应：
    状态行 --> 协议，状态码 404 200
    响应头 --> 放一些客户端使用的一些附加信息
    响应体 --> 服务器返回的真正客户端要用的内容(HTML,json)等
"""
import random
mrd = random.random()
print(mrd)
url = "https://pearvideo.com/category_loading.jsp?reqType=5&categoryId=5&start=72&mrd=0.5085245939105579"


name = '现场 | 中国首家未来零售空间HAUS SHANGHAI进驻淮海路商圈'
if "|" in name:
    print("wo yao")
video_name = name.replace("|", " ") + '.mp4'
print(video_name)

