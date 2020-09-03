import random

from selenium import webdriver

import time

browser = webdriver.Chrome()
browser.get("http://cqwz.cqnews.net/index")

ids=""
button1 = browser.find_elements_by_css_selector(".ask a")
print(button1)
button1[1].click()
flag = True
count=0
while(flag):
    time.sleep(1)
    button = browser.find_element_by_class_name('page-more')
    count=count+1
    print(count)
    button.click()
    if count==3:
        flag=False
lis = browser.find_elements_by_css_selector('.askTitle a')
for l in lis:
    print(l.get_attribute('href'))

# with open("G:/516/学姐/url3.txt", 'a', encoding="utf-8")as f:
#     for l in lis:
#         f.write(l.get_attribute('href'))
#         f.write("\n")
#         print(l.text)
# f.close()