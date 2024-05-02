calculator_ascii = """
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b

def calculate():
    print(calculator_ascii)
    running = True
    first_number = int(input("What's the first number?: "))
    while running:

        operation = input("\n + \n - \n * \n / \n Pick an operation?: ")
        second_number = int(input("What's the second number?: "))
        result = 0
        if operation == "+":
            result = addition(first_number, second_number)
        elif operation == "-":
            result = subtraction(first_number, second_number)
        elif operation == "*":
            result = multiplication(first_number, second_number)
        elif operation == "/":
            result = division(first_number, second_number)
        else:
            print("Invalid operation!")
        print(f"{first_number} {operation} {second_number} = {result}")

        command = input(f"Type 'y' to continue calculating with {result}, or type 'n' to end.")
        if command == "n":
            running = False
        else:
            first_number = result


if __name__ == "__main__":
    calculate()

