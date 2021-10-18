name = str(input("Enter the name:"))
roll = int(input("Enter the roll number:"))
marks = int(input("Enter the marks scored:"))

with open("record.bin", "wb") as file:
    
    file.write(f"{name},{roll},{marks}\n".encode('utf8'))
    
with open("record.bin", "r+b") as file:
    data = file.read().decode('utf8')
    
    if (str(roll) in data):
        marks += 100
        file.write(f"{name},{roll},{marks}".encode('utf8'))
        print("Record Updated")
    else: 
        print("invalid roll number")
