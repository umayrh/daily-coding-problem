"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where
each element is unit-width wall and the integer is the height. Suppose it will rain and all spots
between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3
in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8
units of water.
"""
from typing import List
Vector = List[int]


def _volume(vec: Vector, st: int, en: int) -> int:
    print(f"{st}, {en}: {vec[st:en]}")
    if st >= en - 1:
        return 0
    min_vol = min(vec[st], vec[en -1])
    volume = 0
    for idx in range(st, en):
        volume += max(min_vol - vec[idx], 0)
    return volume


def integrate(vec: Vector):
    vec_len = len(vec)
    if not vec or vec_len <= 2:
        return 0
    idx = 1
    idx_st = 0
    volume = 0
    # Discount for the trough at the beginning of the sequence
    while idx < vec_len and vec[idx] >= vec[idx_st]:
        idx += 1
    idx_st = idx - 1
    # Starting from the top of the first trough
    while idx < vec_len:
        if vec[idx] >= vec[idx_st]:
            # Find the end of the trough
            while idx < vec_len and vec[idx] >= vec[idx_st]:
                idx += 1
            volume += _volume(vec, idx_st, idx)
            # The end of one abyss is the beginning of another
            idx_st = idx - 1
        idx += 1
    print(f"volume: {volume}")
    return volume


if __name__ == "__main__":
    assert integrate([2, 1, 2]) == 1
    assert integrate([3, 0, 1, 3, 0, 5]) == 8

    assert integrate([1, 2, 3, 4, 5]) == 0
    assert integrate([5, 4, 3, 2, 1]) == 0
    assert integrate([2, 1, 2, 1, 2, 1]) == 2
