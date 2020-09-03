# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
import json
from qiluminsheng.items import QiluminshengItem

class qilvminshengspider(scrapy.Spider):
    i=200000
    name = 'qilvminsheng'
    #allowed_domains = ['qlms.dzwww.com']
    start_urls = ["http://qlms.dzwww.com/threadlist.php?filter=echo&page=1"]

#http://cqwz.cqnews.net/ask/askDetail?id=259781

    def parse(self, response):

        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        index= soup.select("tbody")
        for i in index:
            print(i['id'])
        url=soup.select(".folder a")
        title=soup.select(".subject a")
        flag=soup.select(".subject span")
        if self.i < 10:
            self.i += 1
            page ="http://qlms.dzwww.com/threadlist.php?filter=echo&page="+str(self.i)
            yield scrapy.Request(page, callback=self.parse, dont_filter=True)
               # url跟进结束
