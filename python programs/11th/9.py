string = input("Enter Your String : ")

vowels = consonants = uppercase = lowercase = 0

vowels_list = ['a','e','i','o','u']

for i in string:

   if i in vowels_list:

       vowels += 1

   if i not in vowels_list:

       consonants += 1

   if i.isupper():

        uppercase += 1

   if i.islower():

        lowercase += 1

 

print("Number of Vowels in this String = ", vowels)

print("Number of Consonants in this String = ", consonants)

print("Number of Uppercase characters in this String = ", uppercase)

print("Number of Lowercase characters in this String = ", lowercase)
