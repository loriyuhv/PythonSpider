from itemadapter import ItemAdapter
import json
import csv
import pymysql
import os


class Sun0769Pipeline:
    
    def __init__(self):
        # 获取当前目录路径
        # self.current_path = os.getcwd()
        # 获取上一级目录路径
        self.up_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    def process_item(self, item, spider):
        if spider.name == "sun":
            # 写入CSV，文件名：data
            # self.write_csv(item, name="data")
            # 写入JSON，文件名：data
            # self.write_json(item, name="data")
            # 写入mysql
            self.write_mysql(item)
        return item

    def write_mysql(self, item):
        # 链接数据库，创建对象db
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="12345",
            database="test03",
            port=3306
        )
        # 创建游标
        cursor = db.cursor()

        # 创建数据库data
        sql = "CREATE TABLE IF NOT EXISTS data (" \
              "`编号` VARCHAR(255), `状态` VARCHAR(255)," \
              "`问政问题` VARCHAR(255), `响应时间` VARCHAR(255)," \
              "`问政时间` VARCHAR(255), `链接` VARCHAR(255)" \
              ")"
        cursor.execute(sql)
        
        # 插入数据
        sql01 = "INSERT INTO data(`编号`, `状态`, `问政问题`, `响应时间`, `问政时间`, `链接`) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql01, (item["number"], item["status"],
                               item["title"], item["resp_time"], item["req_time"], item["link"]))
        # 提交命令
        db.commit()
        
        # 关闭数据库
        db.close()

    def write_json(self, item, name):
        path = self.up_path + "/sources/data/%s.json" % name
        with open(path, mode='at', encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False) + ",\n")

    def write_csv(self, item, name):
        file_full_path = self.up_path + "/sources/data/%s.csv" % name
        if os.path.exists(file_full_path):
            with open(file_full_path, mode="at", encoding='gbk') as f:
                writer = csv.writer(f)
                writer.writerow([item["number"], item["status"], item["title"],
                                 item["resp_time"], item["req_time"], item["link"]])
        else:
            with open(file_full_path, mode='wt', encoding='gbk') as f:
                writer = csv.writer(f)
                writer.writerow(["编号", "状态", "问政问题", "响应时间", "问政时间", "链接"])
            with open(file_full_path, mode="at", encoding='gbk') as f:
                writer = csv.writer(f)
                writer.writerow([item["number"], item["status"], item["title"],
                                 item["resp_time"], item["req_time"], item["link"]])
