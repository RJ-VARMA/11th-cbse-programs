with open("sample.txt","r") as file:
    
    arr = file.readlines()
    dump = open('dump.txt','w+')
    for i in arr:
        if 'a' in i:
            i = i.replace('a','')
            dump.write(i)
    dump.close()
