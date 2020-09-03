# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiluminshengPipeline(object):
    def process_item(self, item, spider):
        with open("G:/516/学姐/qiluminshengurl.txt") as f:
            f.write(item["title"]+"\n")
            f.flush()
            f.close()
        return item
