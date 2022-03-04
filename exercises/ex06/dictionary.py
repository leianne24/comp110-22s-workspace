"""A series of functions for testing."""
__author__ = "730308277"


def invert(list_o: dict[str, str]) -> dict[str, str]:
    """Given a str,str dict, this will return the inverted str,str dict."""
    i_list = {}
    for key in list_o:
        if list_o[key] in i_list:  
            raise KeyError("duplicate value")
        i_list[list_o[key]] = key
    return i_list
    
   
def favorite_color(color_d: dict[str, str]) -> str:
    """A function to return the most repeated color."""
    color_d2 = {}
    for color in color_d:
        if color_d[color] in color_d2:
            color_d2[color_d[color]] += 1
        else:
            color_d2[color_d[color]] = 1
    max_val: int = 0
    fav_col: str = ""
    for color in color_d2:
        if max_val < color_d2[color]:
            max_val = color_d2[color]
            fav_col = color 
    return fav_col


def count(l_one: list[str]) -> dict[str, int]:
    """Will take the list and make a dictionary where the key is the str and the value counts its appearnce times!"""
    dnry = {}
    for item in l_one: 
        if item in dnry:
            dnry[item] += 1
        else:
            dnry[item] = 1   
    return dnry
    # from exercises.ex06.dictionary import count
    # count("turtle", "dog", "turtle", "rabbit")
    # count(["red", "orange", "yellow", "red", "green", "orange" ])