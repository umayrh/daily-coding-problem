"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of
minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house
with kth color, return the minimum cost which achieves this goal.
"""
import sys
from typing import List, Set

Matrix = List[List[int]]
IntSet = Set[int]


def _min_cost_housing(costs: Matrix, house_st_idx: int, excluded_colors: IntSet):
    # No cost to build a non-existent house
    if house_st_idx >= len(costs):
        return 0
    min_cost = sys.maxsize
    for color_idx in range(len(costs[0])):
        if color_idx not in excluded_colors:
            cost_color_idx = costs[house_st_idx][color_idx] + \
                             _min_cost_housing(costs, house_st_idx + 1, excluded_colors.union([color_idx]))
            min_cost = min(min_cost, cost_color_idx)
    return min_cost


def min_cost_housing(costs: Matrix):
    """
    :param costs: N by K matrix of cost of building house of a given color
    :return: minimum cost to build
    """
    return _min_cost_housing(costs, 0, set())


if __name__ == "__main__":
    costs = [[1, 10], [1, 10]]
    assert min_cost_housing(costs) == 11

    costs = [[1], [1]]
    assert min_cost_housing(costs) == sys.maxsize

    costs = [[1, 10, 100], [100, 10, 1]]
    assert min_cost_housing(costs) == 2
