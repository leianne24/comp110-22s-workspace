"""The testing of functions."""
__author__ = "730308277"

from utils import only_evens, sub, concat


def test_only_evens_two() -> None:
    """To test if our only_evens function will return the even values."""
    assert only_evens([8, 6, 9, 4, 7, 10]) == [8, 6, 4, 10]


def test_only_evens() -> None:
    """To test if our only_evens function will return the even values."""
    assert only_evens([1, 2, 4]) == [2, 4]


def test_only_evens_empty() -> None:
    """To test if our only_evens function will return an empty string."""
    assert only_evens([]) == []


def test_sub_two() -> None:
    """To test if our sub function will return the indexed values."""
    assert sub([2, 4, 6, 8, 10], 3, 4) == [8]


def test_sub() -> None:
    """To test if our sub function will return the proper values."""
    assert sub([1, 2, 4], 0, 4) == [1, 2, 4]


def test_sub_empty() -> None:
    """To test our only_evens function will an empty string."""
    assert sub([], 0, 1) == []


def test_concat_two() -> None:
    """To test our only_evens function will return the proper values."""
    assert concat([3, 6, 9], [5, 6, 9, 5]) == [3, 6, 9, 5, 6, 9, 5]


def test_only_concat() -> None:
    """To test our only_evens function will return the proper values."""
    assert concat([8, 6, 4, 2], [1, 3, 5, 7]) == [8, 6, 4, 2, 1, 3, 5, 7]


def test_concat_empty() -> None:
    """To test our only_evens function will an empty string."""
    assert concat([], []) == []

# # python -m pytest exercises/ex05
# # one edge case and two use cases
# # python -m pytest exercises/ex05 
# # from utils import only_evens
# # from utils import sub
# # from utils import concat