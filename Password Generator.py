#Random Password Generator script 

#library
import random

#a list of values that will used 
pass1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","v","p","q","r","s","t","u","v","w","x","y","z", 
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
         "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#is an empty frame where will store values
password = " "

#for loop that will randomly choose 16 values from pass1
for x in range(16):
    password = password + random.choices(pass1)[0]

#print the random values that was stored in password
print('Your new password is: \n',password)

