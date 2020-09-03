# # -*- coding: utf-8 -*-
# import scrapy
# import bs4
# import re
# import json
# from qinghaigovzang.items import QinghaigovzangItem
#
#
# class qinghaigovspider(scrapy.Spider):
#     i = 1
#     url = ""
#     urls = []
#     with open("D:/白玉杰/孙老师/青海政府网/青海政府url/政府理论-治国理论url.txt", encoding="utf-8")as f:
#         urls = f.readlines()
#
#     name = 'qinghaigovzang'
#     allowed_domains = ['qhtibetan.com']
#     start_urls = ["https://www.qhtibetan.com/content/5c9980c6e138231adfac7548.html"]
#
#     def parse(self, response):
#         data = response.body
#
#         soup = bs4.BeautifulSoup(data, "html.parser")
#         #print(soup)
#         title=soup.select("#article_detail > h1")
#         print(title)
#         content=soup.select(".content p")
#         text=""
#         for p in content:
#             print(p.text)
#             text=text+p.text
#         #print(content)
#         item = QinghaigovzangItem()
#         item['title'] = title[0].text
#         item['text'] = text
#         yield item
#
#         if self.i < self.urls.__len__():
#         #if self.i < 3:
#             self.i += 1
#             print("正在爬取第  " + str(self.i)+" 条")
#             url = self.urls[self.i].strip()
#             yield scrapy.Request(url, callback=self.parse, dont_filter=True)
#             # url跟进结束
