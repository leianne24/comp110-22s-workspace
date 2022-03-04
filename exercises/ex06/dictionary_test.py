"""A series of tests for the matching functions!"""
__author__ = "730308277"

from dictionary import count, favorite_color, invert


def test_count_a() -> None:
    """To test if our count function will return the a dictionary with the list frequncies."""
    assert count(["turtle", "dog", "turtle", "rabbit"]) == {'turtle': 2, 'dog': 1, 'rabbit': 1}


def test_count_b() -> None:
    """To test if our count function will return a dictionary with the number of times each value appears."""
    assert count(["red", "orange", "yellow", "red", "green", "orange"]) == {'red': 2, 'orange': 2, 'yellow': 1, 'green': 1}


def test_count_edge() -> None:
    """To test if our count function will return an empty list."""
    assert count([]) == {}


def test_favorite_colors_a() -> None:
    """To test if our color function will return the most popular color of blue."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_colors_b() -> None:
    """To test if our color function will return the most popular color of green."""
    assert favorite_color({"Maria": "green", "Emma": "green", "Adina": "blue", "Shaney": "blue", }) == "green"


def test_favorite_colors_edge() -> None:
    """To test if our color function will return an empty string."""
    assert favorite_color({}) == ""


def test_invert_a() -> None:
    """To test if our invert function will invert these integers."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_b() -> None:
    """To test if our invert function will invert these strings."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_edge() -> None:
    """To test if our color function will return the most popular color of blue."""
    assert invert({}) == {}
# python -m pytest exercises/ex06