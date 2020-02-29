"""
Suppose you are given a table of currency exchange rates, represented as a 2D array.
Determine whether there is a possible arbitrage: that is, whether there is some sequence of
trades you can make, starting with some amount A of any currency, so that you can end up
with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
"""
import sys
from typing import List
Matrix = List[List[int]]


def arbitrage(costs: Matrix) -> int:
    """
    st A B C A
    :param costs:
    :return:
    """
    rows = len(costs)
    cols = len(costs[0])
    distance: Matrix = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
    for st in range(rows):
        queue = [st]
        while len(queue) > 0:
            pass
    pass


if __name__ == "__main__":
    assert arbitrage([[1, 2], [0.3, 1]]) > 0
