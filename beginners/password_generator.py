import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '(', ')']


def password_generator():
    print("Welcome to the PyPassword Generator!")
    letters_count = int(input("How many letters would you like in your password? "))
    symbols_count = int(input("How many symbols would you like in your password? "))
    numbers_count = int(input("How many numbers would you like in your password? "))

    rand_letters = []
    rand_symbols = []
    rand_numbers = []

    while letters_count > 0:
        rand_letters.append(random.choice(letters))
        letters_count -= 1

    while symbols_count > 0:
        rand_symbols.append(random.choice(symbols))
        symbols_count -= 1

    while numbers_count > 0:
        rand_numbers.append(random.choice(numbers))
        numbers_count -= 1

    password_arr = rand_letters + rand_symbols + rand_numbers
    random.shuffle(password_arr)
    password = "".join(password_arr)
    print(password)


if __name__ == '__main__':
    password_generator()
