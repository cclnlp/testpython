# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from mytourspider.mytourspider.items import MytourspiderItem

class TourspiderSpider(scrapy.Spider):
    name = 'tourspider'
    allowed_domains = ['cncn.com']
    f = open("D:/mydata3/beijing.txt", 'r', encoding='utf-8').readlines()
    #print("!"*10,f[0].strip().replace("\"",""))
    i=0
    start_urls = [f[i].strip().replace("\"","")]
# sdsddddddd
    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        h=self.f[self.i].strip().replace("\"","")
        name=h.split("/")
        index=name[name.__len__()-1]
        #print("###################",name[name.__len__()-1])
        # item = MytourspiderItem()
        item['href']=index
        title = soup.select('.header p')
        item['title'] = title[0].text

        picture = soup.select('.banner_con img')

        item['picture'] = picture[0]['src']
        bb =soup.select(".info_list b")
        concon = soup.select(".info_list .con")
        i=0
        for b in bb:
            #print(b.text)
            if b.text=="景点地址":
                item['address']=concon[i].text
            if b.text=="门票信息":
                item['ticket']=concon[i].text
            if b.text=="开放时间":
                item['time']=concon[i].text
            if b.text=="交通指南":
                item['traffic']=concon[i].text.replace("\n","").replace("\r","")
            if b.text=="简介":
                item['abstract']=concon[i].text.replace("\r","")
            i=i+1
        surr=soup.select(".swiper-wrapper a p")
        item['surrounding']=str(surr).replace("\n","")
        # yield item
        if self.i < 1582:
            self.i += 1
            print(str(self.i))
            page =self.f[self.i].strip().replace("\"","")
            yield scrapy.Request(page, callback=self.parse, dont_filter=True)
                # url跟进结束
