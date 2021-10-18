import random
import time
print("Press CTRL + c to Stop the Dice")
play="y"
while play == "y":
    try:
        while True:
            for i in range(10):
                print()
            n = random.randint(1,6)
            print(n,end='')
            time.sleep(.00001)
    except KeyboardInterrupt:
        print("Your Number is :",n)
        ans = input("Play more?(Y):")
        if(ans.lower!='Y'):
            play = 'n'
            break
