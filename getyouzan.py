import random
import xlrd
import xlwt
from selenium import webdriver

import time

browser = webdriver.Chrome()
browser.get("https://account.youzan.com/")

aaa  = browser.find_element_by_css_selector(".qrcode")
aaa.click()
time.sleep(1)

userinput=browser.find_element_by_name("phoneInfo")
time.sleep(2)
userinput.send_keys("13430918079")

time.sleep(2)
inputpass = browser.find_element_by_name("password")
inputpass.send_keys("shiyue123123")
time.sleep(1)
subotton=browser.find_element_by_class_name("zent-btn-primary")
subotton.click()
time.sleep(6)
print("jijiangjinqu")
clickchoose=browser.find_element_by_class_name("dp-title")
print("查找成功")
clickchoose.click()
print("完成点击")
time.sleep(2)
print("全部结束")
myuser=browser.find_element_by_link_text("客户")
myuser.click()
print("点击客户成功")
time.sleep(4)
print("完成等待")
browser.find_element_by_class_name("X9Vy").click()
time.sleep(3)
print("完成最后处理")
i=0
error=0

book = xlwt.Workbook()  # 新建一个excel
sheet = book.add_sheet('有赞数据')  # 添加一个sheet页
count=0
while i<100:

    texts=browser.find_element_by_class_name("zent-grid-tbody").find_elements_by_class_name("zent-grid-tr")
    for text in texts:
        count=count+1
        cc=count
        #print(text.text)
        try:
            customerinfoname = text.find_element_by_class_name("customer-info__name")
            if "VIP" in customerinfoname.text:
                name = str(customerinfoname.text).split("VIP")[0]
                viplevel = "VIP"+str(customerinfoname.text).split("VIP")[1]
            else:
                name = str(customerinfoname.text)
                viplevel = ""
            mobile = text.find_element_by_class_name("customer-info__mobile").text
            card = text.find_elements_by_class_name("zent-grid-td")[2].text
            score = text.find_elements_by_class_name("zent-grid-td")[3].text
            money = text.find_elements_by_class_name("zent-grid-td")[4].text
            info5 = text.find_elements_by_class_name("zent-grid-td")[5].text
            info6 = text.find_elements_by_class_name("zent-grid-td")[6].text
            info7 = text.find_elements_by_class_name("zent-grid-td")[7].text
            sheet.write(count, 0, name)  # Excel第一行第一列写入姓名
            sheet.write(count, 1, viplevel)
            sheet.write(count, 2, mobile)
            sheet.write(count, 3, card)
            sheet.write(count, 4, score)
            sheet.write(count, 5, money)
            sheet.write(count, 6, info5)
            sheet.write(count, 7, info6)
            sheet.write(count, 8, info7)
            book.save( "C:/Users/Administrator/Desktop/有赞最终.xls")  # 微软的office不能用xlsx结尾的，wps随意
            c=count
            print("成功插入"+str(c)+"条记录")
            # with open("C:/Users/Administrator/Desktop/aaaAA.txt","a",encoding="utf-8")as f:
            #     f.write("customerinfoname:"+customerinfoname.text+"\n")
            #     f.write("mobile:"+mobile.text + "\n")
            #     f.write("card:"+card.text + "\n")
            #     f.write("score:"+score.text + "\n")
            #     f.write("money:"+money.text + "\n")
            #     f.write("info5:"+info5.text + "\n")
            #     f.write("info6:"+info6.text + "\n")
            #     f.write("info7:"+info7.text + "\n")
            #     f.write("\n"+10*"#"+str(i)+"\n")
            #     f.flush()
            #     f.close()
        except:
                error=error+1
                print("第"+str(i)+"页出现错误，序号为"+str(cc)+"。共出现"+str(error)+"个由于昵称解析错误!!")
                continue

    # for text in texts:
    #     print(text.text)
    i=i+1
    print(str(i)+"____________________________")
    flag=2
    if i in range(5,52) :
        flag=3
    else:
        flag=2
    browser.find_elements_by_class_name("zent-pagination-arrow-button")[flag].click()
    print("第"+str(i)+"页完成。。。")
    time.sleep(1)

# browser.find_element_by_class_name("X9Vy ZhO0").click()
# print("keyi")

# i=0
# with open("G:/516/学姐/齐鲁民生过滤掉保密url.txt",encoding='utf-8')as f:
#         lines=f.readlines()
#         while(True):
#             #print(lines[i])
#             l=lines[i].split("]")
#             #print(l)
#             #browser.close()
#             #print(l[1].strip())
#             browser.get(l[1].replace("\n","").strip())
#             title=browser.find_element_by_id("threadtitle")
#             tit=str(title.text).replace("\n","")
#             print("title"+tit)
#             print(tit.split(":")[1])
#             body=browser.find_element_by_id("postlist")
#             t=str(body.text)
#             # t=t.replace("1#","").replace("跳转到 »","").replace("倒序看帖","").replace("打印","").replace("字体大小:","")
#             # t=t.replace("t","").replace("T","")
#             #print(t.split(tit.split(":")[1])[1])
#             question=t.split(tit.split(":")[1])[1].split("签收状态")[0]
#             ans=t.split(tit.split(":")[1])[1].split("只看该作者")[1]
#             answer=ans.split("引用")[0]
#             print("question:"+question.replace("\n",""))
#             print("answer:"+answer.replace("\n",""))
#             print("歇息5秒")
#             with open("G:/516/学姐/齐鲁民生/"+str(i)+".txt","a",encoding="utf-8")as f:
#                 f.write("title"+tit+"\n")
#                 f.write("question:"+question.replace("\n","")+"\n")
#                 f.write("answer:"+answer.replace("\n","")+"\n")
#                 f.flush()
#             f.close()
#             time.sleep(1)
#             i=i+1
