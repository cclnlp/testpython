# # -*- coding: utf-8 -*-
# import scrapy
# import bs4
# import re
# import json
# from qinghaigovzang.items import QinghaigovzangItem
#
#
# class qinghaigovspider(scrapy.Spider):
#     i = 99
#     name = 'qinghaigovzang'
#     allowed_domains = ['qh.gov.cn']
#     start_urls = ["http://www.qh.gov.cn/zwgk/xwdt/jqgz/"]
#
#     def parse(self, response):
#
#         data = response.body
#
#         soup = bs4.BeautifulSoup(data, "html.parser")
#         # print(soup)
#         urls = soup.select(".item a")
#         # print(urls)
#         for url in urls:
#             print(url["href"])
#             item = QinghaigovzangItem()
#             item['url'] = url["href"]
#             yield item
#         if self.i > 0:
#             # if self.i <1674:
#             print("现在爬取到第  " + str(self.i) + "  页！！！！！！！！！！！！！")
#             self.i -= 1
#             temp = self.i / 10
#             a = int(temp)
#             # https://www.qhtibetan.com/channel/597a95ff1fd5073e48bb2272.html?p=2
#             #http://www.qh.gov.cn/zwgk/system/more/202010000000000/0016/202010000000000_00001674.shtml
#             #http://www.qh.gov.cn/zwgk/system/more/202030000000000/0000/202030000000000_00000009.shtml
#             #http://www.qh.gov.cn/zwgk/system/more/202040000000000/0005/202040000000000_00000519.shtml
#             #http://www.qh.gov.cn/zwgk/system/more/202090000000000/0002/202090000000000_00000282.shtml
#             page = "http://www.qh.gov.cn/zwgk/system/more/202090000000000/0000"+str(a)+"/202090000000000_000000" + str(
#                 self.i) + ".shtml"
#             yield scrapy.Request(page, callback=self.parse, dont_filter=True)
#             # url跟进结束
