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
#     name = 'qinghaigovzang'
#     allowed_domains = ['qhtibetan.com']
#     start_urls = ["https://www.qhtibetan.com/channel/59ded4279843930288026816.html"]
#
#     def parse(self, response):
#
#         data = response.body
#
#         soup = bs4.BeautifulSoup(data, "html.parser")
#         # print(soup)
#         urls = soup.select(".heading a")
#         print(urls)
#         for url in urls:
#             print(url["href"])
#             item = QinghaigovzangItem()
#             item['url'] ="https://www.qhtibetan.com"+url["href"]
#             yield item
#
#         if self.i <7:
#             print("现在爬取到第  "+str(self.i) +"  页！！！！！！！！！！！！！")
#             self.i += 1
#             #https://www.qhtibetan.com/channel/597a95ff1fd5073e48bb2272.html?p=2
#             page = "https://www.qhtibetan.com/channel/59ded4279843930288026816.html?p=" + str(self.i)
#             yield scrapy.Request(page, callback=self.parse, dont_filter=True)
#             # url跟进结束
