import random

cards_ascii = r"""
     .-~~-.
    {      }
 .-~-.    .-~-.
{              }
 `.__.'||`.__.'
       ||
      '--`


     /\
   .'  `.
  '      `.
<          >
 `.      .'
   `.  .'
     \/


       /\
     .'  `.
    '      `.
 .'          `.
{              }
 ~-...-||-...-~
       ||
      '--`


 .-~~~-__-~~~-.
{              }
 `.          .'
   `.      .'
     `.  .'
       \/
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def score(cards_dealt):

    if sum(cards_dealt) == 21 and len(cards_dealt) == 2:
        return 0

    if 11 in cards_dealt and sum(cards_dealt) > 21:
        cards_dealt.remove(11)
        cards_dealt.append(1)

    return sum(cards_dealt)


def compare(your_score, computer_score):
    if your_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose! Computer has a Blackjack."
    elif your_score == 0:
        return "You win! You have a Blackjack."
    elif your_score > 21:
        return "You lose! Your score is over 21."
    elif computer_score > 21:
        return "You win! Computer score is over 21."
    elif your_score > computer_score:
        return "You win! Your score is over computer."
    else:
        return "You lose! Computer score is over yours."


def blackjack():
    print(cards_ascii)
    end_game = False
    your_cards = []
    computer_cards = []

    # Deal initial cards
    for _ in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"Your cards: {your_cards}")
    print(f"Computer cards: {computer_cards[0]}")

    while not end_game:
        your_score = score(your_cards)
        computer_score = score(computer_cards)

        if your_score == 0 or computer_score == 0 or your_score > 21:
            end_game = True
        else:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")

            if deal_again == 'y':
                your_cards.append(deal_card())
            else:
                end_game = True
        while computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = score(computer_cards)
        print(f"Your cards: {your_cards}")
        print(f"Computer cards: {computer_cards}")
        print(compare(your_score, computer_score))