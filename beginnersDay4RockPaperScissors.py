# Day 4 Exercise : Rock Paper Scissors
import random

# rock wins against scissors
# paper wins against rock
# scissors wins against paper
def rock_paper_scissors():
    rock = '''
             _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        '''
    paper = '''
             _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
        '''
    scissors = '''
             _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        '''
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")
    choice_int = int(choice)
    if choice_int == 0:
        user_choice = 'Rock'
        print(rock)
    elif choice_int == 1:
        user_choice = 'Paper'
        print(paper)
    else:
        user_choice = 'Scissors'
        print(scissors)
    print(f"You Chose: {user_choice}")

    random_number = random.randint(0, 2)
    if random_number == 0:
        computer_choice = 'Rock'
        print(rock)
    elif random_number == 1:
        computer_choice = 'Paper'
        print(paper)
    else:
        computer_choice = 'Scissors'
        print(scissors)
    print(f"Computer Chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        print("You Lose!")
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        print("You Win!")
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print("You Win!")
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print("You Lose!")
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print("You Lose!")
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print("You Win!")
    else:
        print('Error!')
