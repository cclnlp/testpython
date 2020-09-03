# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
import json
from xizangnews.items import XizangnewsItem


class xizangnews(scrapy.Spider):
    i = 1
    errcode=[404,500,302]
    errcount=0
    url = ""
    urls= []
    names=""
    name = 'xizangnews'
    allowed_domains = ['xzxw.com']
    start_urls = ["http://tb.xzxw.com/xw/gngj/gn/201812/t20181231_2489761.html"]

    with open("G:/思思/2018的藏url.txt",encoding="utf-8")as f:
        urls=f.readlines()
    def parse(self, response):
        if response.status in self.errcode:
            if self.i <self.urls.__len__():
            #if self.i < 5:
                print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！出现错误，正在跳过处理！")
                with open("G:/思思/errlog2018zang.txt","a",encoding="utf-8")as f:
                    f.write("现在爬取到第  " + str(self.i) + "  页！:"+self.urls[self.i]+"出现错误，正在跳过处理！状态码："+str(response.status)+"\n")
                    f.flush()
                    f.close()
                self.i += 1
                self.errcount=self.errcount+1
                url = self.urls[self.i].strip()
                yield scrapy.Request(url, callback=self.parse, dont_filter=True)
        else:
            try :
                data = response.body
                soup = bs4.BeautifulSoup(data, "html.parser")
                t1 = soup.select(".first_title")[0].text
                t2 = soup.select(".second_title")[0].text
                t3 = soup.select(".third_title")[0].text
                title=t1+t2+t3
                print(title)

                times=soup.select(".item_content")[0].text

                time="2018"+str(times).split("2018")[1]
                print(time)

                text= soup.select(".sj4_abstract_content p")
                texts=""
                for p in text:
                    texts=texts+p.text
                print(texts)
                item = XizangnewsItem()
                item['title'] = title
                item['text'] = texts.replace("\n","")
                item['time'] =time
                item['url'] =response.url
                yield item

                if self.i <self.urls.__len__():
                #if self.i < 5:
                    print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！")
                    print("出错个数为："+str(self.errcount)+"!!!!!!!!!!!!!!!")
                    self.i += 1
                    url = self.urls[self.i].split("#")[0].strip()
                    yield scrapy.Request(url, callback=self.parse, dont_filter=True)
                    # url跟进结束
            except:
                if self.i < self.urls.__len__():
                    # if self.i < 5:
                    print("现在爬取到第  " + str(self.i) + "  页！！！出现错误解析，正在跳过处理！")
                    with open("G:/思思/errlog2018zang.txt", "a", encoding="utf-8")as f:
                        f.write("现在爬取到第  " + str(self.i) + "  页！:"+self.urls[self.i]+"出现错误，正在跳过处理！解析方式异常或网页异常\n")
                        f.flush()
                        f.close()
                    self.i += 1
                    self.errcount = self.errcount + 1
                    url = self.urls[self.i].split("#")[0].strip()
                    yield scrapy.Request(url, callback=self.parse, dont_filter=True)
