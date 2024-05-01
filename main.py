from beginners.generate_band_name import generate_band_name
from beginners.tip_calculator import tip_calculator
from beginners.treasure_island import treasure_island
from beginners.rock_paper_scissors import rock_paper_scissors
from beginners.password_generator import password_generator


def main():
    print("Select a programme to run with its respective number:")
    selection = int(input("    Beginners: [0] Generate Band Name \n"
                          "    Beginners: [1] Tip Calculator \n"
                          "    Beginners: [2] Treasure Island \n"
                          "    Beginners: [3] Rock Paper Scissors \n"
                          "    Beginners: [4] Password Generator \n"))
    if selection == 0:
        generate_band_name()
    elif selection == 1:
        tip_calculator()
    elif selection == 2:
        treasure_island()
    elif selection == 3:
        rock_paper_scissors()
    elif selection == 4:
        password_generator()
    else:
        print("Invalid selection")


if __name__ == "__main__":
    main()
