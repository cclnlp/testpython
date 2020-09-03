with open("G:/516/学姐/urlqilu.txt",encoding='utf-8')as f:
    lines=f.readlines()
    for line in lines:
        print(line)
        if "保密" in line:
            print('这个保密')
        else :
            with open("G:/516/学姐/urlqiludeal.txt","a",encoding="utf-8") as fwrite:
                fwrite.write(line)
            fwrite.close()
f.close()