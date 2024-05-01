import random

hangman_ascii = r''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

hangman_ascii_full = [r'''

     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
  ___|___

''',
                      r'''

     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
  ___|___

''',
                      r'''

     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
  ___|___

''',
                      r'''

     _________
     |/      |
     |      (_)
     |      \|/
     |       
     |     
     |
  ___|___

''',
                      r'''

     _________
     |/      |
     |      (_)
     |      \|
     |      
     |      
     |
  ___|___

''',
                      r'''

     _________
     |/      |
     |      (_)
     |       |
     |       
     |     
     |
  ___|___

''',
                      r'''

     _________
     |/      |
     |      (_)
     |      
     |       
     |      
     |
  ___|___

''',
                      r'''

     _________
     |/      |
     |      
     |      
     |       
     |      
     |
  ___|___

'''
                      ]

words = [
    "Finitely",
    "Misleading",
    "Dinning",
    "Energizing",
    "Untruest",
    "Menorah",
    "Ghoulish",
    "Realism",
    "Caliphate",
    "Buttercup",
    "Oratorio",
    "Prefix",
    "Gaming",
    "Preshrunk",
    "Harmed",
    "Loop",
    "Banknote",
    "Doily",
    "World"
]


def hangman():
    word = random.choice(words).lower()
    blanks = []
    life = 7
    for _ in word:
        blanks.append('_')

    while life >= 0:
        guess = input("Guess a letter: ").lower()
        for position in range(len(word)):

            if guess == word[position]:
                blanks[position] = guess

        if guess not in word:
            print(hangman_ascii_full[life])
            print("Oh no. Wrong guess!")
            life -= 1
        if "_" not in blanks:
            print(blanks)
            print("You guessed the word!")
            return
        if life < 0:
            if "_" in blanks:
                print("You lost! The word was " + word)
        print(blanks)


if __name__ == '__main__':
    hangman()
