"""
Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given `[6, 1, 3, 3, 3, 6, 6]`, return 1. Given `[13, 19, 13, 13]`, return 19.

Do this in O(N) time and O(1) space.
"""
from typing import List
Vector = List[int]


def not_a_triplet(vec: Vector):
    product = 1
    cube_product = 1
    for item in vec:
        product *= item
        cube_product *= item ** (1/3)
    return 1


if __name__ == "__main__":
    assert not_a_triplet([6, 1, 3, 3, 3, 6, 6]) == 1
    assert not_a_triplet([13, 19, 13, 13]) == 19
