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
#     name = 'xizangnews'
#     allowed_domains = ['xzxw.com']
#     start_urls = ["http://www.xzxw.com/xw/gnyw/"]
#     myurl = "http://www.xzxw.com/xw/gnyw"
#
#     def parse(self, response):
#         data = response.body
#         soup = bs4.BeautifulSoup(data, "html.parser")
#         urls = soup.select(".visit_detail li a")
#
#         for url in urls:
#             time = url.select("span")[0].text
#             item = XizangnewsItem()
#             item["time"]=time
#             item['url'] ="http://www.xzxw.com/xw" + str(url["href"]).replace("../../","/").replace("../","/")
#             yield item
#         if self.i <2817:
#             print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！")
#             self.i += 1
#             page = self.myurl+"/index_" + str(self.i) + ".html"
#             yield scrapy.Request(page, callback=self.parse, dont_filter=True)
#             # url跟进结束
