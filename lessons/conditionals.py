"""Conditional Statements, if-else (an example)"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input ("What is your guess? "))

if guess == SECRET: 
    print("you guessed correctly!!")
    print("have a wonderful day... or else")
else: 
    print("LAME")
    if guess > SECRET:
        print("Guess lower")
    else:
        print("guess higher")

print("Game over.")
