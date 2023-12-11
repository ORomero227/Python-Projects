'''Password Generator Program'''
import random as rnd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator")

letter_qty = int(input("How many letter would you like in your password?\n"))
symbols_qty = int(input("How many symbols would you like?\n"))
numbers_qty = int(input("How many numbers would you like>\n"))

random_choices = []
password = ""

# Random letters
for char in range(1, letter_qty + 1):
    random_choices.append(rnd.choice(letters))

# Random symbols
for char in range(1, symbols_qty + 1):
    random_choices.append(rnd.choice(symbols))

# Random numbers
for char in range(1, numbers_qty + 1):
    random_choices.append(rnd.choice(numbers))

# Shuffle list
rnd.shuffle(random_choices)

# Create the password
for char in random_choices:
    password += char

print(f"Your password is: {password}")
