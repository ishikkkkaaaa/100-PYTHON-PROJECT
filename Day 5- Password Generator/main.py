#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#start with an empty password
first=""
for i in range(0,nr_letters):
     #random_char=random.choice(letters)
     first+=random.choice(letters)

second=""
for i in range(0,nr_symbols):
     #random_char=random.choice(letters)
     second+=random.choice(symbols)

third=""
for i in range(0,nr_numbers):
     #random_char=random.choice(letters)
     first+=random.choice(numbers)

password=first+second+third
print(password)
print(type(password))
str_var = list(password)
random.shuffle(str_var)
print(type(str_var))
print (type(''.join(str_var)))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
""" final=random.shuffle(password)
print(f"Your password is: {final}") """


