"""A One Shot Wordle!"""

__author__ = "730308277"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input("What is your 6-letter guess? ")
word: str = "python"

while len(guess) != len(word):
    guess = input("That was not 6 letters! Try again: ")

emoji: str = "" 
index: int = 0
if word == guess:
        print ("Woo! You got it!")
else:
    print ("Not quite. Play again soon!")
while index < len(guess):
    if word[index] == guess[index]:
        emoji = emoji + GREEN_BOX
    else:
        j: int = 0
        bool_found: bool = False
        while j < len(word):
            if word[j] == guess[index]:
                bool_found = True
            j = j + 1
        if bool_found == True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index = index + 1
print(emoji)






"""
while len(guess) == len(word):
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji: str = ""     
    while index <= len(word):
        while word[index] == guess[index]:
            emoji: str = GREEN_BOX
            print(emoji)
        while word[index] != guess[index]:
            index = index + 1
            emoji: str = WHITE_BOX
"""