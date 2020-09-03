# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class XizangnewsPipeline(object):
    # def process_item(self, item, spider):
    #     #print("开始写入*******************************")
    #     with open("G:/思思/myurl.txt","a",encoding="utf-8") as f:
    #         f.write(item["url"]+"#"+str(item["time"]) + "\n")
    #         f.flush()
    #         f.close()
    #     return item
    # def process_item(self, item, spider):
    #     #print("开始写入*******************************")
    #     with open("C:/Users/Administrator/Desktop/藏/新闻汉text/"+item["name"]+"text.txt","a",encoding="utf-8") as f:
    #         f.write("="*60 + "\n")
    #         f.write("title:"+item["title"]+"\n")
    #         f.write("text:"+item["text"]+"\n")
    #         f.flush()
    #         f.close()
    #     return item
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='', db='2018_tibetan_news',charset='utf8',
                     use_unicode=True, port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # sql语句
        insert_sql = """insert into tibetan_news(title,content,time,url) VALUES(%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql,
                            (pymysql.escape_string(item['title']), pymysql.escape_string(item['text']), item['time'], item['url']))
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()













