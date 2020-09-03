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
    with open("G:思思/2018segcontent思思.txt","r",encoding="utf-8") as f:
        content=f.read()
        #ccc=re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", content)  # 去标点符号
        print(content)
        seg_list =content.split(" ")
        c = Counter()
        for x in seg_list:
            if len(x) > 1 and x != '\r\n':
                c[x] += 1
        print('常用词频度统计结果')
        lenth=len(c)
        for (k, v) in c.most_common(len(c)):
            with open("G:思思/2018zangcontresult.txt","a",encoding="utf-8")as w:
                mm = v/lenth
                w.write(str(k)+" "+str(mm)+"\n")
            print(str(k)+"    "+str(v) )


if __name__ == '__main__':

        get_words()
