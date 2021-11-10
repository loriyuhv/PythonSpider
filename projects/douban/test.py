import json
import os
import csv



# name = "data"
# # print(os.getcwd())
# fileFullPath = os.getcwd() + "\%s.csv" % name
# print(fileFullPath)
# if os.path.exists(fileFullPath):
#     if os.path.exists(fileFullPath):
#         os.remove(fileFullPath)
# else:
#     with open("data.csv", 'wt', encoding='utf8') as f:
#         writer = csv.writer(f)
#         writer.writerow(["编号", "状态", "问政问题", "响应时间", "问政时间", "链接"])

from urllib.parse import urlencode

# data = {
#     "name": "Jerry",
#     "page": 1
# }

# params = urlencode(data)
# print(params)
data = b'{"name": "Walker", "age": 19}'
# data = {"name": "Jerry", "age": 18}
data1 = open('test.json', 'ab+')
    # f.seek(-10, 2)

json.dump(data, ensure_ascii=False, fp=data1)


# with open("test.json", 'ab', encoding='utf-8') as f:



# import json
#
#
# class ZhipinspiderPipeline(object):
# # 初始化要写入的JSON文件（Window默认字符集为GBK，建议以二进制的形式输出并编码成UTF-8格式）
# def __init__(self):
#     self.json_file = open('jobs.json', 'wb+')
#     self.json_file.write('\n'.encode('UTF-8'))
#
# def process_item(self, item, spider):
#     # 将每个item对象转换成一个json字符串
#     text = json.dumps(dict(item), ensure_ascii=False) + ',\n'
#     # 写入JSON文件
#     self.json_file.write(text.encode('UTF-8'))
#
# # 蜘蛛关闭时（自动调用close_spider方法），需要关闭文件
# def close_spider(self, spider):
#     print('-------关闭文件-------')
#     self.json_file.seek(-2, 1)
#     self.json_file.write('\n'.encode('UTF-8'))
#     self.json_file.close()
