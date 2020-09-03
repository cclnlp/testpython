# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
import json
# from beijingtour.items import BeijingtourItem

class beijing(scrapy.Spider):
    i=1
    name = 'beijingtour'
    #allowed_domains = ['cqwz.cqnews.net']
    start_urls = ["https://m.cncn.com/jingdian/beijing?show_zone_option_list=1&use_ajax=1&typeid=0&star=0&page=1"]

#http://cqwz.cqnews.net/ask/askDetail?id=259781

    def parse(self, response):

        data = response.body
        soup = BeautifulSoup(data, "html.parser")

        url=soup.select("a")
        #print(url)
        with open("D:/mydata3/beijing.txt","a",encoding="utf-8") as f:
            for u in url:
                print(u['href'])
                f.write('https://m.cncn.com'+u['href']+'\n')
                f.flush()
        f.close()
        if self.i < 159:
            self.i += 1
            page ="https://m.cncn.com/jingdian/beijing?show_zone_option_list=1&use_ajax=1&typeid=0&star=0&page="+str(self.i)
            yield scrapy.Request(page, callback=self.parse, dont_filter=True)
               # url跟进结束
