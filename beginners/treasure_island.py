# Day 3 Exercise : Treasure Island
def treasure_island():
    print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."-.______ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
    print("Welcome to the Treasure Island.")
    print("Your mission is to find treasure.")
    left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right \n")
    if left_or_right == "left":
        swim_or_wait = input("You come to a lake. There is an island in middle of the lake. "
                             "Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
        if swim_or_wait == "wait":
            red_yellow_or_blue = input("You arrive at the island unharmed. There is a house with 3 doors. One red, "
                                       "one yellow and one blue. Which colour do you choose?")
            if red_yellow_or_blue == "yellow":
                print("You win.")
            else:
                print("Oh no! You got attacked by a dragon. Game over.")
        else:
            print("Oh no! You got attacked by a dragon. Game over.")
    else:
        print("Oh no! You got attacked by a dragon. Game over.")


if __name__ == '__main__':
    treasure_island()
