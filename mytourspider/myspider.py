#！/user/bin/env python
# _*_coding:utf _*_
import json
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
# @File  : myspider.py
# @Author: Baiyujie
# @Date  : 2018/11/10
# @Software: PyCharm
# 旅游景点的分类链接的爬取

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html,"html.parser")
    aa =soup.select("a")
    for a in aa:
        print(a["href"])
        write_to_file(a["href"])



def write_to_file(content):
    with open('C:/Users/Administrator/Desktop/新建文件夹/瀑布url.txt', 'a', encoding='utf-8') as f:
        #https://m.cncn.com/jingdian/42134
        f.write(json.dumps("https://m.cncn.com"+content, ensure_ascii=False) + '\n')
        f.close()

def main():
    for i in range(50):
        offset=str(i)
        url = 'https://m.cncn.com/jingdian/jingdian_list?show_zone_option_list=1&use_ajax=1&typeid=3&star=0&page=' + offset
        print(url)

        html = get_one_page(url)
        parse_one_page(html)

if __name__ == '__main__':
    main()

