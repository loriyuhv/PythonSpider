import csv
import json
import pymysql
import os


class DoubanPipeline:

    def process_item(self, item, spider):
        self.write_json(dict(item))
        return item

    def write_json(self, item):
        name = "douban250"
        with open("%s.json" % name, mode='at', encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False) + ",\n")


# class SunPipeline:
#
#     def __init__(self):
#         self.current_path = os.getcwd()
#
#     def process_item(self, item, spider):
#         if spider.name == "sun":
#             self.write_csv(item, name="data")
#             self.write_json(item, name="data")
#             self.write_mysql(item, name="data")
#         return item
#
#     def write_mysql(self, item, name):
#         db = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="12345",
#             database="test",
#             port=3306
#         )
#         cursor = db.cursor()
#         sql = "CREATE TABLE IF NOT EXISTS %s" % name + " (" \
#               "`编号` VARCHAR(255), `状态` VARCHAR(255)," \
#               "`问政问题` VARCHAR(255), `响应时间` VARCHAR(255)," \
#               "`问政时间` VARCHAR(255), `链接` VARCHAR(255)" \
#               ")"
#         cursor.execute(sql)
#         sql1 = "INSERT INTO data(`编号`, `状态`, `问政问题`, `响应时间`, `问政时间`, `链接`) VALUES(%s, %s, %s, %s, %s, %s)"
#         cursor.execute(sql1, (item["number"], item["status"], item["title"], item["resp_time"],
#                               item["req_time"], item["link"]))
#         db.commit()
#         db.close()
#
#     def write_json(self, item, name):
#         with open("%s.json" % name, mode='at', encoding='utf-8') as f:
#             f.write(json.dumps(item, ensure_ascii=False) + ",\n")
#
#     def write_csv(self, item, name):
#         file_full_path = self.current_path + "/%s.csv" % name
#         if os.path.exists(file_full_path):
#             with open("%s.csv" % name, mode="at", encoding='gbk') as f:
#                 writer = csv.writer(f)
#                 writer.writerow([item["number"], item["status"], item["title"],
#                                  item["resp_time"], item["req_time"], item["link"]])
#         else:
#             with open("%s.csv" % name, mode='wt', encoding='gbk') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(["编号", "状态", "问政问题", "响应时间", "问政时间", "链接"])
#             with open("%s.csv" % name, mode="at", encoding='gbk') as f:
#                 writer = csv.writer(f)
#                 writer.writerow([item["number"], item["status"], item["title"],
#                                  item["resp_time"], item["req_time"], item["link"]])
