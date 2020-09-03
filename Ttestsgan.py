img=[]
with open("G:/doublecar/PB/Wifi上位机（新）/上位机源代码SuperMonitor/SuperMonitor/bin/Release/Data/mykc20190622(4).txt","r",encoding="utf-8")as f:
    lines=f.readlines()
    for line in lines:
        #print(line)
        strimg =line.split("85 170 255 162")[1].split("240")[0]
        #print(strimg)
        huifuimg=strimg.split("255 ")
        for hh in huifuimg:
            #print(hh)
            imgperline=[]
            imgadges=hh.split()
            c=1
            for iii in imgadges:
                c=c+1
                flag=c % 2  #取余运算
                count=int(iii)
                for i in range(count):
                    imgperline.append(str(flag))
                if len(imgperline)<100:
                    for ccc in range(100-len(imgperline)):
                        imgperline.append(str(1))
                #print("imgperline"+str(imgperline))
                with open("G:/doublecar/PB/Wifi上位机（新）/上位机源代码SuperMonitor/SuperMonitor/bin/Release/Data/处理mykc20190622(4).txt","a",encoding="utf-8")as f:
                    for abcc in imgperline:
                        #if
                    f.write(str(imgperline)+"\n")
                    f.flush()
                    f.close()


            #     for imgadge in imgadges:
            #         imgadgeint=int(imgadge)
            #         if i==imgadgeint:
            #             flag=flag+1
            #     if flag==0:
            #         imgperline.append("0")
            #
            # for h in hh.split():
            #     inth=int(h)
            #


        # straaa=strimg.split()
        # print("原始"+str(straaa))
        # print(straaa[2:])
        # img=straaa
