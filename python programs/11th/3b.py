def numpat(n):
    num = 1
    for i in range(n,0,-1):
        num = 1
        for j in range(1, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5
numpat(n)
