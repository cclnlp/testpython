# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy

class MytourspiderPipeline(object):
    """
           功能：保存item数据
    """
    n=""
    c=""
    def __init__(self):
        self.filename = open("D:/mydata3/tourtext430.txt", "a",encoding="utf-8")
    def process_item(self, item, spider):
        print(spider.name)
        #text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        title=item["title"]
        self.filename.write(title+'##address##' + str(item["address"]).replace("\n","") +"$"+ "\n")
        self.filename.write(title+'##picture##' + item["picture"] +"$"+ "\n")
        self.filename.write(title+'##ticket##' + item["ticket"]+"$" + "\n")
        self.filename.write(title+'##time##' + item["time"]+"$" + "\n")
        self.filename.write(title+'##traffic##' + str(item["traffic"]).replace("'","").replace("\n","") +"$"+ "\n")

        if item["surrounding"] is not None:
            ss=str(item["surrounding"]).replace("<p>","").replace("</p>","").replace("[","").replace("]","").replace("'","").split(", ")
            for s in ss:
                self.filename.write(title+'##surrounding##' + s +"$"+ "\n")
        self.filename.write("$" + title + '##abstract##' + str(item["abstract"]).replace("\n", "") + "$" + "\n")

        self.filename.flush()
        #self.filename.close()
        with open("D:/mydata3/tourtextab430.txt", "a",encoding="utf-8")as ab:
            ab.write("$"+title + '##abstract##' + str(item["abstract"]).replace("\n","") +"$"+ "\n")
            ab.flush()
            ab.close()
        return item
    def close_spider(self, spider):
        print(spider.name)
        self.filename.close()

