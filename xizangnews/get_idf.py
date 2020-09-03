import re

import pymysql
import jieba
import jieba.posseg as pseg
from collections import Counter
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
        print(line[1])

    cursor.close()
    connect.close()
def get_words():
    with open("G:思思/2018content.txt","r",encoding="utf-8") as f:
        content=f.read()
        ccc=re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", content)  # 去标点符号
        seg_list = jieba.cut(ccc)
        c = Counter()
        for x in seg_list:
            if len(x) > 1 and x != '\r\n':
                c[x] += 1
        print('常用词频度统计结果')
        lenth=len(c)
        for (k, v) in c.most_common(len(c)):
            with open("G:思思/2018contentresult.txt","a",encoding="utf-8")as w:
                mm = v/lenth
                w.write(str(k)+" "+str(mm)+"\n")
            print(str(k)+"    "+str(v) )
#zh_topic_2018_one

def dealmysqltable():
    connect = pymysql.connect(host='localhost', user='root', password='', db='2018_tibetan_news', charset='utf8', use_unicode=True,
                              port=3306)
    cursor = connect.cursor()

    select_sql = """select * from tibetan_news"""

    cursor.execute(select_sql)
    col = cursor.description
    result = cursor.fetchall()
    print("我是col", col)
    for line in result:
        #print(line)
        title=line[0]
        content=line[1]
        zh_title=pseg.cut(title)
        zh_content=pseg.cut(content)


        zh_title_fen=""
        zh_content_fen = ""
        zh_title_biaozhu=""
        zh_content_biaozhu=""
        for x in zh_title:
            zh_title_fen += "{} ".format(x.word)
            zh_title_biaozhu += "{}/{} ".format(x.word, x.flag)
        print(zh_title_fen)
        print(zh_title_biaozhu)
        print("------------------------------------")

        for x in zh_content:
            zh_content_fen += "{} ".format(x.word)
            zh_content_biaozhu += "{}/{} ".format(x.word, x.flag)
        print(zh_content_fen)
        print(zh_content_biaozhu)
        print("------------------------------------")



        insert_sql = """insert into zh_new_process_2018(zh_title_fen,zh_content_fen,zh_title_biaozhu,zh_content_biaozhu,zh_title,zh_content,zh_time,zh_url) 
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(insert_sql,(zh_title_fen,zh_content_fen,zh_title_biaozhu,zh_content_biaozhu,line[0],line[1],line[2],line[3]))
        # 提交，不进行提交无法保存到数据库
        connect.commit()




    cursor.close()
    connect.close()

if __name__ == '__main__':

        #get_words()
        dealmysqltable()