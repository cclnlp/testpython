# -*- coding: utf-8 -*-
import requests
import re
import pymysql

def seg(s):
    if s.strip()!="":
        url='http://10.10.130.152:5000/seg_ti'
        input=s
        data={
            "seg_string":input
        }
        res=requests.post(url=url,json=data)

        return  res.json()['result']

def dealmysqltable():
    connect = pymysql.connect(host='localhost', user='root', password='', db='2018_tibetan_news', charset='utf8', use_unicode=True,
                              port=3306)
    cursor = connect.cursor()

    select_sql = """select * from tibetan_news"""
    cursor.execute(select_sql)
    col = cursor.description
    result = cursor.fetchall()
    print("我是col", col)
    i=0
    with open("G:思思/2018segcontent思思.txt","a",encoding="utf-8")as fw:
        for i in range(len(result)):
            if i>3936:
                print("正在处理第" + str(i) + "行！！！")
                title=result[i][0]
                content=result[i][1]
                time=result[i][2]
                url=result[i][3]
                i=i+1
                fen=str(seg(title+"#######"+content))

                zw_title_fen=fen.split("#######")[0]
                zw_content_fen=fen.split("#######")[1]
                print("第"+str(i)+"次请求实验室服务器分词成功：" + fen)
                fw.write(zw_content_fen+"\n")
                fw.flush()
                zw_title_biaozhu=" "
                zw_content_biaozhu=" "
                zw_title=title
                zw_content=content
                zw_time=time
                zw_url=url
                print("正在插入数据库。。。")
                insert_sql = """insert into tibetan_news_process(zw_title_fen,zw_content_fen,zw_title_biaozhu,zw_content_biaozhu,zw_title,zw_content,zw_time,zw_url) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(insert_sql,(zw_title_fen,zw_content_fen,zw_title_biaozhu,zw_content_biaozhu,zw_title,zw_content,zw_time,zw_url))
                # 提交，不进行提交无法保存到数据库
                connect.commit()
            else:
                i=i+1
                print("第"+str(i)+"行已经写入，跳过处理")

        cursor.close()
        connect.close()
if __name__ == '__main__':

    dealmysqltable()