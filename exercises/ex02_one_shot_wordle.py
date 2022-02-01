"""A One Shot Wordle!"""

__author__ = "730308277"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

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
        emoji = emoji + green_box
    else:
        j: int = 0
        bool_found: bool = False
        while j < len(word):
            if word[j] == guess[index]:
                bool_found = True
            j = j + 1
        if bool_found == True:
            emoji = emoji + yellow_box
        else:
            emoji = emoji + white_box
    index = index + 1
print(emoji)