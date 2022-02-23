"""An example of list utility functions and testing."""
__author__ = "730308277"


def only_evens(evens: list[int]) -> list[int]:
    """This fuction should return only the even numbers."""
    elist: list[int] = []
    i: int = 0
    while len(evens) > i: 
        if evens[i] % 2 == 0:
            elist.append(evens[i])
        i += 1
    return elist 

# def sub(list: list[int]) -> list[int]: 