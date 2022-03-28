"""Dictionary related utility functions."""

__author__ = "730308277"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # close the file when we're done, to free its resources 
    for row in csv_reader:
        result.append(row)

    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """We want to take a list and turn it into a colunm, with it's name as the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(not_m: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """A function to check the first few rows of a table to make sure we aren't screwing up too badly."""
    result: dict[str, list[str]] = {}
    for column in not_m:
        first_n: list[str] = []
        i: int = 0
        if len(not_m[column]) < rows:
            rows = len(not_m[column])
        while i < rows:
            item = not_m[column][i]
            first_n.append(item)
            i += 1
        result[column] = first_n
    return result 
# use a while loop
#  use for in loop for the list of data, not fro the dictionary. We
# while loop in for loop, shortening the list parts 
# while i is l


def select(orignal: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Give a lot of columns and data, this will return only the columns you desire."""
    result: dict[str, list[str]] = {}
    for column in orignal: 
        for name in col_names: 
            if name == column:
                result[name] = orignal[column]
    return result


def concat(set_one: dict[str, list[str]], set_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce one table by combining two column based tables."""
    result: dict[str, list[str]] = {}
    for column in set_one:
        result[column] = set_one[column]
    for column in set_two:
        if column in result: 
            # result[column] += set_two[column]
            for item in set_two[column]:  
                result[column].append(item)
        else:
            result[column] = set_two[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """With a list[str] we will get a dictionary where each key is one of the strings, and the value is how many times that key appears."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 