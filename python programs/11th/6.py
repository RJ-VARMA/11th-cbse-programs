import math

n = int(input("Enter a Number:"))

if n < 2:
    print("A number must be 2 and more")
    quit()
elif n == 2:
    print("It's prime number")
    quit()

i = 2
limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("This is composite number")
        quit()
    i += 1

print("It's prime number")
