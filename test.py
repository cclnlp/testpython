# -*- coding: utf-8 -*-
import requests
import pymysql
def getfrommysql():
    connect = pymysql.connect(host='localhost', user='root', password='', db='2018_tibetan_news', charset='utf8',
                                       use_unicode=True, port=3306)
    cursor =connect.cursor()

    select_sql = """select * from tibetan_news"""

    cursor.execute(select_sql)
    col = cursor.description
    result = cursor.fetchall()
    print("我是col",col)
    for line in result:
        print(line[0])
        print(line[1])
        with open("G:思思/aaa.txt","a",encoding="utf-8")as f:
            f.write(line[0]+"#######"+line[1]+"$$$$$$$$$"+"\n")
            f.flush()
            f.close()

    cursor.close()
    connect.close()
def seg(s):
    if s.strip()!="":
        url='http://10.10.130.152:5000/seg_ti'
        input=s
        data={
            "seg_string":input
        }
        res=requests.post(url=url,json=data)
        return  res.json()['result']

if __name__ == '__main__':
    getfrommysql()