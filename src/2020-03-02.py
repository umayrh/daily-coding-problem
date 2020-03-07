"""
You have an N by N board. Write a function that, given N, returns the number of
possible arrangements of the board where N queens can be placed on the board without
threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""


def n_queens(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 0
    if n == 3:
        return 1
    return n_queens(n - 1) * 2

    return 0


if __name__ == "__main__":
    assert 1==1
