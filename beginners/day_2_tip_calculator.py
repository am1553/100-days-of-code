# Day 2 Exercise : Tip Calculator
def tip_calculator():
    print("Welcome to the tip calculator!")
    total_bill = input("What's the total bill?")
    tip_percent = input("How much tip would you like to give? 10%, 12%, or 15%?")
    people = int(input("How many people to split the bill?"))
    bill_per_person = "{:.2f}".format(round(float(total_bill) * (int(tip_percent) / 100 + 1) / people, 2))
    print(f"Each person should pay: ${bill_per_person}")
    exit()