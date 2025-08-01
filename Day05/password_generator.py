import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
# random_string = "".join(random.choice(letters) for _ in range(nr_letters))
#
# random_symbol = "".join(random.choice(symbols) for _ in range(nr_symbols))
#
# random_numbers = "".join(random.choice(numbers) for _ in range(nr_numbers))
#
# password = str(random_string) + str(random_symbol) + str(random_numbers)
#
# print(password)

#hard level

random_string = "".join(random.choice(letters) for _ in range(nr_letters))

random_symbol = "".join(random.choice(symbols) for _ in range(nr_symbols))

random_numbers = "".join(random.choice(numbers) for _ in range(nr_numbers))

password = str(random_string) + str(random_symbol) + str(random_numbers)

char_list = list(password)
random.shuffle(char_list)
shuffled_string = "".join(char_list)

print(f"Your Password: {shuffled_string}")