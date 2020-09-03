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
#     start_urls = ["http://www.xzxw.com/xw/shengthb/201903/t20190328_2567146.html"]
#     # filename="生态环保"
#     # with open("C:/Users/Administrator/Desktop/藏/新闻汉url/"+filename+"url.txt",encoding="utf-8")as f:
#     #     urls=f.readlines()
#     with open("G:/思思/2018.txt",encoding="utf-8")as f:
#         urls=f.readlines()
#     def parse(self, response):
#         if response.status in self.errcode:
#             if self.i <self.urls.__len__():
#             #if self.i < 5:
#                 print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！出现错误，正在跳过处理！")
#                 with open("G:/思思/errlog2018.txt","a",encoding="utf-8")as f:
#                     f.write("现在爬取到第  " + str(self.i) + "  页！:"+self.urls[self.i]+"出现错误，正在跳过处理！状态码："+str(response.status)+"\n")
#                     f.flush()
#                     f.close()
#                 self.i += 1
#                 self.errcount=self.errcount+1
#                 url = self.urls[self.i].split("#")[0].strip()
#                 yield scrapy.Request(url, callback=self.parse, dont_filter=True)
#         else:
#             try :
#                 data = response.body
#                 soup = bs4.BeautifulSoup(data, "html.parser")
#                 # print(soup)
#                 time=self.urls[self.i].split("#")[1].strip()
#                 t=time.split("日")
#                 tim=t[0].replace("年","-").replace("月","-")
#                 title = soup.select(".tbig_title h1")
#                 text= soup.select(".xw_daodu_detail p")
#                 texts=""
#                 for p in text:
#                     texts=texts+p.text
#                 item = XizangnewsItem()
#                 item['title'] = title[0].text.strip()
#                 item['text'] = texts.replace("\n","")
#                 item['time'] =tim
#                 item['url'] =response.url
#                 yield item
#
#                 if self.i <self.urls.__len__():
#                 #if self.i < 5:
#                     print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！")
#                     print("出错个数为："+str(self.errcount)+"!!!!!!!!!!!!!!!")
#                     self.i += 1
#                     url = self.urls[self.i].split("#")[0].strip()
#                     yield scrapy.Request(url, callback=self.parse, dont_filter=True)
#                     # url跟进结束
#             except:
#                 if self.i < self.urls.__len__():
#                     # if self.i < 5:
#                     print("现在爬取到第  " + str(self.i) + "  页！！！出现错误解析，正在跳过处理！")
#                     with open("G:/思思/errlog2018.txt", "a", encoding="utf-8")as f:
#                         f.write("现在爬取到第  " + str(self.i) + "  页！:"+self.urls[self.i]+"出现错误，正在跳过处理！解析方式异常或网页异常\n")
#                         f.flush()
#                         f.close()
#                     self.i += 1
#                     self.errcount = self.errcount + 1
#                     url = self.urls[self.i].split("#")[0].strip()
#                     yield scrapy.Request(url, callback=self.parse, dont_filter=True)
