import random

from selenium import webdriver

import time

browser = webdriver.Chrome()
browser.get("http://qlms.dzwww.com/viewthread.php?tid=33906&extra=")

input = browser.find_element_by_css_selector(".postbox .txt")
time.sleep(1)
input.send_keys("bai123456789")
time.sleep(2)
inputpass = browser.find_element_by_id("password3")
inputpass.send_keys("123456789")
time.sleep(1)
subotton=browser.find_element_by_class_name("submit")
subotton.click()
time.sleep(5)
i=0
with open("G:/516/学姐/齐鲁民生过滤掉保密url.txt",encoding='utf-8')as f:
        lines=f.readlines()
        while(True):
            #print(lines[i])
            l=lines[i].split("]")
            #print(l)
            #browser.close()
            #print(l[1].strip())
            browser.get(l[1].replace("\n","").strip())
            title=browser.find_element_by_id("threadtitle")
            tit=str(title.text).replace("\n","")
            print("title"+tit)
            print(tit.split(":")[1])
            body=browser.find_element_by_id("postlist")
            t=str(body.text)
            # t=t.replace("1#","").replace("跳转到 »","").replace("倒序看帖","").replace("打印","").replace("字体大小:","")
            # t=t.replace("t","").replace("T","")
            #print(t.split(tit.split(":")[1])[1])
            question=t.split(tit.split(":")[1])[1].split("签收状态")[0]
            ans=t.split(tit.split(":")[1])[1].split("只看该作者")[1]
            answer=ans.split("引用")[0]
            print("question:"+question.replace("\n",""))
            print("answer:"+answer.replace("\n",""))
            print("歇息5秒")
            with open("G:/516/学姐/齐鲁民生/"+str(i)+".txt","a",encoding="utf-8")as f:
                f.write("title"+tit+"\n")
                f.write("question:"+question.replace("\n","")+"\n")
                f.write("answer:"+answer.replace("\n","")+"\n")
                f.flush()
            f.close()
            time.sleep(1)
            i=i+1
