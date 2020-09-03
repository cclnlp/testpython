# import json
# import re
# def resolvejson(inpath,outpath):
#     with open(inpath,'r',encoding='utf-8')as fin:
#         line =fin.readline()
#         line=line.replace("{","")
#         line= line.replace("\"","")
#         line= line.replace("title","")
#         line = line.replace("[","")
#         line = line.replace("]","")
#         line = line.replace(":","")
#         re.findall("(?<=<).*?(?=>)",line).clear()
#
#         f = open("c:\\1.txt", "r")
#         lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
#         for line in lines
#
#         # line =line.replace(a,"")
#         print(line)
#
#
#
#
# def main():
#     resolvejson("tourtext.json", "finally.json")
#
# if __name__ == '__main__':
#     main()
