# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QinghaigovzangPipeline(object):
    def process_item(self, item, spider):
       # print("开始写入*******************************")
        with open("G:/516/2019年4月语料爬取/青海政府网/青海政府汉text/通知公告.txt","a",encoding="utf-8") as f:
            f.write("="*60+"\n")
            f.write("title:"+item["title"] + "\n")
            f.write("text:" +item["text"] + "\n")
            f.flush()
            f.close()
        return item
    # def process_item(self, item, spider):
    #     #print("开始写入*******************************")
    #     with open("C:/Users/Administrator/Desktop/藏/近期关注.txt","a",encoding="utf-8") as f:
    #         f.write(item["url"] + "\n")
    #         f.flush()
    #         f.close()
    #     return item



