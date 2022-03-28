"""An example of union types."""
# lets us specify types

from typing import Union


def log(info: Union[int, str]) -> None:
    """Log is a function that can be calld with _either_ an int or a str argument."""
    if isinstance(info, str): 
        print(f"str: {info}")
    else:
        print(f"int: {info}")


log("Hello, World")
log(110)