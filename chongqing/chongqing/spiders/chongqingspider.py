# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
import json
from chongqing.items import ChongqingItem

class chongqingspider(scrapy.Spider):
    i=200000
    name = 'chongqing'
    #allowed_domains = ['cqwz.cqnews.net']
    start_urls = ["http://cqwz.cqnews.net/ask/askDetail?id=259781"]

#http://cqwz.cqnews.net/ask/askDetail?id=259781

    def parse(self, response):

        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        title=soup.select(".wenShowTitle")[0].text
        question=soup.select(".wenShowTitle5")[0].text
        answers=soup.select(".wenShowLeft p")
        ans=''
        for answer in answers:
            ans=ans+answer.text
            #print(ans)

        item = ChongqingItem()
        item['index']=str(self.i)
        item['title']=title
        item['question']=question
        item['answer']=ans

        yield item
        #print(item)
        # url跟进开始
        # 获取下一页的url信息
        # url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        # if url:
        #     # 将信息组合成下一页的url
        if self.i < 300000:
            self.i += 1
            page ="http://cqwz.cqnews.net/ask/askDetail?id="+str(self.i)
            yield scrapy.Request(page, callback=self.parse, dont_filter=True)
               # url跟进结束
