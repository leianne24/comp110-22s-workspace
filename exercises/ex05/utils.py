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


def sub(a_list: list[int], s: int, e: int) -> list[int]: 
    """Will give you whichever parts of a list you give an index of."""
    b_list: list[int] = []
    if s < 0:
        s = 0
    i: int = s
    e = e - 1
    while e > i:
        
        if e > len(a_list):
            e = len(a_list)
    b_list.append(a_list[i])  
    i += 1
    return b_list


# from exercises.ex05.utils import only_evens
# from exercises.ex05.utils import sub  