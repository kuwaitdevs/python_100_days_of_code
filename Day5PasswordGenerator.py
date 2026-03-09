import random

letters =   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']
numbers =   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols =   ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")

num_of_letters = int(input("How many letters do you want in your password?\n> "))
num_of_symbols = int(input("How many symbols do you want in your password?\n> "))
num_of_numbers = int(input("How many numbers do you want in your password?\n> "))

final_password = []

if(num_of_letters > 0):
    for letter in range(0, num_of_letters):
         random_index = random.randint(0, len(letters) - 1)
         final_password.append(letters[random_index])

if(num_of_symbols > 0):
    for symbol in range(0, num_of_symbols):
         random_index = random.randint(0, len(symbols) - 1)
         final_password.append(symbols[random_index])

if(num_of_numbers > 0):
    for num in range(0, num_of_numbers):
         random_index = random.randint(0, len(numbers) - 1)
         final_password.append(numbers[random_index])

final_password_shuffled = []

while len(final_password) > 0:
    random_index = random.randint(0, len(final_password) - 1)
    random_char = final_password.pop(random_index)
    final_password_shuffled.append(random_char)

print("Your super duper password is:")
for char in final_password_shuffled:
    print(char, end="")

print("")