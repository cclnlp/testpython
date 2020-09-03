import random

from selenium import webdriver

import time
flag=0
browser = webdriver.Chrome()
browser.get("http://qlms.dzwww.com/threadlist.php?filter=echo")
with open("G:/516/学姐/urlqilu.txt", 'a', encoding="utf-8")as f:
    while (True):
        time.sleep(1)
        i=0
        lis = browser.find_elements_by_css_selector('.subject')
        href = browser.find_elements_by_css_selector('.subject a')
        for l in lis :
            f.write(lis[i].text+href[i].get_attribute('href')+"\n")
            flag=flag+1
            print(flag)
            f.flush()
            i=i+1
        button = browser.find_elements_by_css_selector(".pages .next")
        button[0].click()
# print(button1)
# button1[1].click()
# while(True):
#
#
#
#     with open("G:/516/学姐/url2.txt", 'a', encoding="utf-8")as f:
#         for l in lis:
#             #print(l.get_attribute('href'))
#             href=str(l.get_attribute('href')).split("=")
#             print(href)
#             id=href[1]
#             #print("我是id"+id)
#             #print("我是列表"+ids)
#             if id in ids:
#                 print(id+"存在")
#             else:
#                 ids=ids+id+"."
#                 f.write(l.get_attribute('href'))
#                 f.write("\n")
#             print(l.text)
#         f.close()
