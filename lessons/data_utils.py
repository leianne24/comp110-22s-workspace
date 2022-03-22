"""Some helpful utility functions for working with CSV Files."""

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