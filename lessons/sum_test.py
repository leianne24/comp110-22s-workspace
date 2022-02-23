"""Tests for the sum function."""
# always use test_ in names, alwasy use _test in the name of the module

from lessons.sum import sum


def test_sum_empty() -> None:
    """To test a list."""
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0

# paramterless, return none (for now)
# python -m pytest lessons/sum_test.py