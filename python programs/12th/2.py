vowels = ["a" ,"e" ,"i" ,"o" ,"u"]

consonants = ["b" ,"c" ,"d" ,"f" ,"g" ,"h" ,"j",
              "k", "l", "m", "n", "p", "q", "r", 
              "s", "t", "v", "w", "x", "y", "z"]

with open("sample.txt", "r") as file:
    
    # Read File
    data = file.read()

    # Initialize counter
    count_c = 0
    count_v = 0
    count_upper = 0
    count_lower = 0
    
    # Loop through Text
    for c in data:
        if (c.islower()):
            count_lower +=1
        elif(c.isupper()):
            count_upper +=1
        c = c.lower()
        if c in vowels:
            count_v += 1
        elif c in consonants:
            count_c += 1

    print(f"""Number of Consonants is {count_c}, Number of Vowels is {count_v}, Number of Uppercase 
            characters is {count_upper}, Number of Lowercase characters is {count_lower}""")
