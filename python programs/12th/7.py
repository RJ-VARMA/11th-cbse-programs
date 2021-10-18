import csv

login = False
answer = input("Do you have an account?(yes or no) ")

if answer == 'yes' :
   with open('upassword.csv', 'r') as csvfile:
      csv_reader = csv.reader(csvfile)
      username = input("Player One Username: ")
      password = input("Player One Password: ")

      for row in csv_reader:
         print(row[0], row[1])
         print(username, password)
         if row[0]== username and row[1] == password:
            login = True
            break
         else:
            login = False
            break

   if login == True:
      print("You are now logged in!")
   else:
      print("Incorrect. Game Over.")
      exit()    
else:
   print('Only Valid Usernames can play. Game Over.')
   exit()
