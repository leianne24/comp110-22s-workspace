"""A realish wordle!"""
__author__ = "730308277" 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Checks to see if a letter is in a word."""
    i: int = 0 
    assert len(character) == 1
    while i < len(word): 
        if word[i] == character:
            return True 
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """This will check to see if the secret and the word have letters in common."""
    assert len(guess) == len(secret)  
    index = 0
    emoji: str = ""
    while index < len(secret):
        if secret[index] == guess[index]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        index += 1
    return emoji 


def input_guess(length: int) -> str:
    """Check's to see if the guess is the right length."""
    attempt: str = input(f"Enter a {length} character word: ")
    while length != len(attempt):
        attempt = input(f"That wasn't {length} chars! Try again: ")
    if length == len(attempt):
        return attempt
    return attempt


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    length: int = len(secret_word)
    i: int = 1
    while i < 7:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(length)
        if secret_word == guess:
            print(emojified(guess, secret_word))
            print(f"You won in {i}/6 turns!")
            i += 6
        else: 
            print(emojified(guess, secret_word))
            if i == 6:
                print("X/6 - Sorry, try again tomorrow!")
        i += 1


if __name__ == "__main__":
    main()