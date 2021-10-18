#Read a text file line by line and display each word seperated by a #

#myfile.txt has following data
"""
welcome to python class
welcome to CBSE class 12 program 15
School programming
"""
fh=open("sample.txt","r")
item=[]
for i in fh:
    words=i.split()
    for j in words:
        item.append(j)
        
print("#".join(item))
