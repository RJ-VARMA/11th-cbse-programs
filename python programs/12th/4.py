name = str(input("Enter the name:"))
roll = int(input("Enter the roll number:"))

with open("sample.bin", "wb") as file:
    file.write(f"{name},{roll}".encode('utf8'))
    
with open("sample.bin", "rb") as file:
    data = file.read().decode('utf8')
    if (name in data) and (str(roll) in data):
        print("Found!")
    else:
        print("Not Found, run again")
