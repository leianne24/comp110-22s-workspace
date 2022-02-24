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
    if e >= len(a_list):
        e = len(a_list) - 1
    else:
        e = e - 1
    while e >= i:
        part: int = (a_list[i])
        b_list.append(part)  
        i += 1
    return b_list


def concat(l_one: list[int], l_two: list[int]) -> list[int]:
    """Will make list two concatenate onto the end of list two."""
    m_list: list[int] = []
    for item in l_one: 
        m_list.append(item)
    for item_t in l_two:
        m_list.append(item_t)
    return m_list


# from exercises.ex05.utils import only_evens
# from exercises.ex05.utils import sub
# from exercises.ex05.utils import concat
# concat([10, 20], [30, 40])