# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import mysql.connector
class PyFilePipeline(object):
    # def process_item(self, item, spider):
    #     print ("序号：",item['Nuber'])
    #     print("代码:", item['fodecode'])
    #     print("名称:", item['Name'])
    #     print("类型:", item['Type'])
    #     print("报告期:", item['ReportDate'])
    #     print("摘要:", item['Abstract'])
    #     print("公告期:", item['DeclarationDate'])

    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root', password='1237646LY',host='localhost', port='3306',database='excells',
            use_unicode=True)
        # 获取数据库操作游标
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        print('----------------------------关闭数据库---------------------------')
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        # self.cur.execute("INSERT INTO fode VALUES(%s,%s,%s,%s,%s,%s,%s)",
        #                  (item['Nuber'], item['fodecode'], item['Name'],
        #                   item['Type'],item['ReportDate'], item['Abstract'],
        #                   item['DeclarationDate']))
        nuberstr=item['Nuber'][0]
        fodecode=item['fodecode'][0]
        Name= item['Name'][0]
        Type= item['Type'][0]
        ReportDate=item['ReportDate'][0]
        Abstract=item['Abstract'][0]
        DeclarationDate=item['DeclarationDate'][0]
        values = [nuberstr, fodecode, Name, Type,ReportDate, Abstract, DeclarationDate]
        self.cur.execute("insert into fode values (%s,%s,%s,%s,%s,%s,%s)", values)
        self.conn.commit()
#定义构造器，初始化预写入的文件
    # def __init__(self):
    #         self.json_file=open("s.json","wb+")
    #         self.json_file.write('\n'.encode("utf-8"))
    # #重写close_spider 回调方法，用于关闭文件
    # def close_spider(self,spider):
    #         print('--------------------------------关闭文件-----------------------------------------------')
    #         #后退两个字符，也就是去掉最后一条记录之后的换行街和逗号
    #         self.json_file.seek(-2,1)
    #         self.json_file.write('\n'.encode("utf-8"))
    #         self.json_file.close()
    # def process_item(self,item,spider):
    #         #将对象转换为JSON字符串
    #         text=json.dumps(dict(item),ensure_ascii=False)+",\n"
    #         #写入JSON字符串
    #         self.json_file.write(text.encode("utf-8"))


