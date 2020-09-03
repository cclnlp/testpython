# # -*- coding: utf-8 -*-
# import scrapy
# import bs4
# import re
# import json
# from xizangnews.items import XizangnewsItem
#
#
# class xizangnews(scrapy.Spider):
#     i = 1
#     errcode=[404,500,302]
#     errcount=0
#     url = ""
#     urls= []
#     names=""
#     name = 'xizangnews'
#     allowed_domains = ['xzxw.com']
#     start_urls = ["http://www.xzxw.com/xw/201904/t20190404_2576544.html"]
#     #filename="生态环保"
#     with open("G:/思思/allurl.txt",encoding="utf-8")as f:
#         urls=f.readlines()
#
#     def parse(self, response):
#         if response.status in self.errcode:
#             if self.i <self.urls.__len__():
#             #if self.i < 5:
#                 print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！出现错误，正在跳过处理！")
#                 with open("G:/思思/errlog.txt","a",encoding="utf-8")as f:
#                     f.write("现在爬取到第  " + str(self.i) + "  页！:"+response.url+"出现错误，正在跳过处理！状态码："+str(response.status)+"\n")
#                     f.flush()
#                     f.close()
#                 self.i += 1
#                 self.errcount=self.errcount+1
#                 url = self.urls[self.i].strip()
#                 yield scrapy.Request(url, callback=self.parse, dont_filter=True)
#         else:
#             try :
#                 data = response.body
#                 soup = bs4.BeautifulSoup(data, "html.parser")
#                 title = soup.select(".tbig_title")
#                 text= soup.select(".xw_daodu_detail p")
#                 r=response.xpath("/html/body/div[5]")
#                 print(r)
#                 time =soup.select("body > div:nth-child(5) > div:nth-child(1)")
#                 print(time)
#                 texts=""
#                 for p in text:
#                     texts=texts+p.text
#                 print(texts)
#                 #print(time[0].text+"*"*20)
#                 # item = XizangnewsItem()
#                 # item['title'] = title[0].text
#                 # item['text'] = texts
#                 # item['name'] =self.filename
#                 # yield item
#
#                 if self.i <self.urls.__len__():
#                 #if self.i < 5:
#                     print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！")
#                     print("出错个数为："+str(self.errcount)+"!!!!!!!!!!!!!!!")
#                     self.i += 1
#                     #print(url+"!"*20)
#                     url = self.urls[self.i].strip()
#                     print(url + "!" * 20)
#                     yield scrapy.Request(url, callback=self.parse, dont_filter=True)
#                     # url跟进结束
#             except:
#                 print("异常！！！！！！！！！！！！！！！！！！！！！")
#                 # if self.i < self.urls.__len__():
#                 #     # if self.i < 5:
#                 #     print("现在爬取到第  " + str(self.i) + "  页！！！出现错误解析，正在跳过处理！")
#                 #     with open("G:/思思/errlog.txt", "a", encoding="utf-8")as f:
#                 #         f.write("现在爬取到第  " + str(self.i) + "  页！:"+response.url+"出现错误，正在跳过处理！解析方式异常或网页异常\n")
#                 #         f.flush()
#                 #         f.close()
#                 #     self.i += 1
#                 #     self.errcount = self.errcount + 1
#                 #     url = self.urls[self.i].strip()
#                 #     yield scrapy.Request(url, callback=self.parse, dont_filter=True)
