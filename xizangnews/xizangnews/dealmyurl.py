years=["2016","2017","2018","2019"]
with open("G:思思/myurl.txt",encoding='utf-8')as f:
    lines=f.readlines()
    for line in lines:
        print(line)
        l=line.split("#")
        for year in years:
            if year in l[1]:
                with open("G:思思/"+year+".txt","a",encoding="utf-8") as fwrite:
                    fwrite.write(line)
                    fwrite.flush()
                    fwrite.close()
f.close()

