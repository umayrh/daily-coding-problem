"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give 2. The input `[1, 2, 0]` should give 3.

You can modify the input array in-place.
"""
from typing import List
Vector = List[int]


def find_missing_int(input: Vector):
    # if sorted, with all negs set to 0:
    #   if pairwise difference in seq <= 1
    #     return max(seq) + 1
    #   else
    #     return min(pair) + 1
    res = 0
    for item in input:
        if item > 0:
            res = res | item
    #


if __name__ == "__main__":
    assert find_missing_int([3, 4, -1, 1]) == 2
    assert find_missing_int([1, 2, 0]) == 3
