gavel_ascii = r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
"""


def blind_auction():
    print(gavel_ascii)
    print("Welcome to the secret auction program.")
    is_new_bidder = True
    auction = {}

    while is_new_bidder:
        name = input("What is your name? ")
        bid = int(input("What is your bid? £"))
        auction[name] = bid
        new_bidder = input("Are there any other bidders? Type 'yes' or 'no' \n")
        if new_bidder != 'yes':
            is_new_bidder = False
    highest_bid = 0
    highest_bidder = ""
    for bidder in auction:
        amount = auction[bidder]
        if highest_bid < amount:
            highest_bid = amount
            highest_bidder = bidder
    print(f"The winner is {highest_bidder.title()} with a bid of £{highest_bid}.")


if __name__ == "__main__":
    blind_auction()
