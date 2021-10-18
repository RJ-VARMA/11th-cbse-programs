print("PATTERN - 1\n")


for i in range (0,5):
    for j in range(0,i+1):
        print("*",end ="")
    print()



print("PATTERN - 2\n")


for i in range (5,0,-1):
    num = 1
    for j in range(1,i+1):        
        print(num,end ="")
        num = num + 1 
    print()

print("PATTERN - 3\n")


for i in range (65,70):
    for j in range(65,i+1):
        print(chr(j),end ="")
    print()
