"""A One Shot Wordle!"""

guess: str = input("What is your 6-letter guess? ")
word: str = ("python")



while len(guess) != len(word):
    guess: str = input("That was not 6 letters! Try again: ")
  

while len(guess) == len(word):
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji: str = ""       
    while index < len(guess):
        while word[index] == guess[index]:
            emoji: str = GREEN_BOX
            index = index + 1
        while word[index] != guess[index]:
            emoji: str = GREEN_BOX
            index = index + 1
            index = index +1 
    while index == len(guess):
        print(f"")
       







__author__ = "730308277"