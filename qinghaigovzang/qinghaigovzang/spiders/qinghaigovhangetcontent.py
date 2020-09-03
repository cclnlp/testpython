
# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
import json
from qinghaigovzang.items import QinghaigovzangItem


class qinghaigovspider(scrapy.Spider):
    i = 0
    errcode = [404, 500, 302]
    errcount = 0
    url = ""
    urls = []
    with open("G:/516/2019年4月语料爬取/青海政府网/青海政府汉url/通知公告.txt", encoding="utf-8")as f:
        urls = f.readlines()

    name = 'qinghaigovzang'
   # allowed_domains = ['qh.gov.cn']
    start_urls = ["http://www.qh.gov.cn/zwgk/system/2019/04/07/010327969.shtml"]

    def parse(self, response):
        print("现在爬取到第  " + str(self.i) + "  页！:"+response.url+str(response.status))
        if response.status in self.errcode:
            if self.i <self.urls.__len__():
            #if self.i < 5:
                print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！出现错误，正在跳过处理！")
                with open("G:/516/2019年4月语料爬取/青海政府网/青海政府汉url/errlog.txt","a",encoding="utf-8")as f:
                    f.write("现在爬取到第  " + str(self.i) + "  页！:"+response.url+"出现错误，正在跳过处理！状态码："+str(response.status)+"\n")
                    f.flush()
                    f.close()
                self.i += 1
                self.errcount=self.errcount+1
                url = self.urls[self.i].strip()
                yield scrapy.Request(url, callback=self.parse, dont_filter=True)
        else:
            try:
                data = response.body

                soup = bs4.BeautifulSoup(data, "html.parser")
                #print(soup)
                title=soup.select(".blue")
                print(title)
                content=soup.select(".details_content p")
                text=""
                for p in content:
                    print(p.text)
                    text=text+p.text
                #print(content)
                item = QinghaigovzangItem()
                item['title'] = title[0].text
                item['text'] = text
                yield item


                if self.i < self.urls.__len__():
                #if self.i < 3:
                    self.i += 1
                    print("正在爬取第  " + str(self.i)+" 条")
                    url = self.urls[self.i].strip()
                    yield scrapy.Request(url, callback=self.parse, dont_filter=True)
                    # url跟进结束
            except:
                if self.i < self.urls.__len__():
                    # if self.i < 5:
                    print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！出现错误，正在跳过处理！")
                    with open("G:/516/2019年4月语料爬取/青海政府网/青海政府汉url/errlog.txt", "a", encoding="utf-8")as f:
                        f.write("现在爬取到第  " + str(self.i) + "  页！:" + response.url + "出现错误，正在跳过处理！状态码：" + str(
                            response.status) + "\n")
                        f.flush()
                        f.close()
                    self.i += 1
                    self.errcount = self.errcount + 1
                    url = self.urls[self.i].strip()
                    yield scrapy.Request(url, callback=self.parse, dont_filter=True)
