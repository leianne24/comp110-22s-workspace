"""A realish wordle!"""
__author__ = "730308277" 

#input_guess emjoified contains_char main



# guess: str = input("What is your 6-letter guess? ")
# word: str = "python"

# while len(guess) != len(word):
#     guess = input("That was not 6 letters! Try again: ")

# emoji: str = "" 
# index: int = 0
# if word == guess:
#     print("Woo! You got it!")
# else:
#     print("Not quite. Play again soon!")
# while index < len(guess):
#     if word[index] == guess[index]:
#         emoji = emoji + green_box
#     else:
#         j: int = 0
#         bool_found: bool = False
#         while j < len(word):
#             if word[j] == guess[index]:
#                 bool_found = True
#             j = j + 1
#         if bool_found == True:
#             emoji = emoji + yellow_box
#         else:
#             emoji = emoji + white_box
#     index = index + 1
# print(emoji)




#we don't need actual character limits in her
# keep things in function
# stick ith return functions as much as psosible

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool: #declare a function
    """checks to see if a letter is in a word"""
    i = 0  #would i: int = 0 also work? Are these interchangable? Also, do I have to delete these for the autograder?
    assert len(character) == 1
    while i < len(word): #We need this just for the while statement, and to make sure someone's word isn't ridivulously small. Should we let them have a one letter word?
        if word[i] == character:
            return True 
        i += 1 #making sure that these are outside the if statement will prevent infintie loop statemints 
    return False

def emojified(guess: str, secret: str) -> str:
    """This will check to see if the secret and the word have letters in common."""
    assert len(guess) == len(secret)  #How do we incorportae contains_char?
    index = 0
    emoji: str = ""
    while index < len(guess):
        emoji = contains_char(guess) # What did I forget here?
        index += 1
    return emoji




        # if guess[index] == secret[index]:
        #     emoji = emoji + GREEN_BOX
        # else:
        #     j: int = 0
        #     bool_found: bool = False
        #     while j < len(guess):
        #         if guess[j] == secret[index]: #wouldn't hte while statement just keep repeating without adding onto the emoji string?
        #             bool_found = True
        #         j = j + 1
        #     if bool_found == True: #why shouldn't these be indented?
        #         emoji = emoji + YELLOW_BOX
        #     else:
        #         emoji = emoji + WHITE_BOX
        # index = index + 1
    return emoji