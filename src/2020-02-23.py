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


def _integrate_trough(vec: Vector, st: int, en: int) -> int:
    print(f"{st}, {en}: {vec[st:en]}")
    if st >= en - 1:
        return 0
    min_vol = min(vec[st], vec[en - 1])
    volume = 0
    for idx in range(st, en):
        volume += max(min_vol - vec[idx], 0)
    return volume


def integrate(vec: Vector):
    vec_len = len(vec)
    if vec_len <= 2:
        return 0
    trough_en = [1, vec_len - 2, 1]
    trough_st = [0, vec_len - 1, 0]
    total_volume = [0, 0, 0]

    # Discount for the unbounded basin at the beginning of the sequence
    while trough_en[0] < vec_len and vec[trough_en[0]] >= vec[trough_st[0]]:
        trough_en[0] += 1
        trough_en[2] += 1
    trough_st[0] = trough_en[0] - 1
    trough_st[2] = trough_en[2] - 1
    # Starting at the end, discount for the unbounded basin at the beginning of the sequence
    while trough_en[1] >= 0 and vec[trough_en[1]] >= vec[trough_st[1]]:
        trough_en[1] -= 1
    trough_st[1] = trough_en[1] + 1

    # Starting from the top of the first trough
    while trough_en[0] < vec_len or trough_en[2] < vec_len or trough_en[1] >= 0:
        # Case 1: a wall at least as high as the start of this trough
        if trough_en[0] < vec_len and vec[trough_en[0]] >= vec[trough_st[0]]:
            # Find the end of the trough
            while trough_en[0] < vec_len and vec[trough_en[0]] >= vec[trough_st[0]]:
                trough_en[0] += 1
            total_volume[0] += _integrate_trough(vec, trough_st[0], trough_en[0])
            # The end of one abyss is the beginning of another
            trough_st[0] = trough_en[0] - 1
        # Case 2: starting at the end, a wall at least as high as the start of this trough
        if trough_en[1] >= 0 and vec[trough_en[1]] >= vec[trough_st[1]]:
            while trough_en[1] >= 0 and vec[trough_en[1]] >= vec[trough_st[1]]:
                trough_en[1] -= 1
            total_volume[1] += _integrate_trough(vec, trough_en[1] + 1, trough_st[1] + 1)
            trough_st[1] = trough_en[1] + 1
        # Case 3: no wall as high as the start but there are intermediate troughs
        if trough_en[2] < vec_len and vec[trough_en[2]] >= vec[trough_en[2] - 1]:
            while trough_en[2] < vec_len and vec[trough_en[2]] >= vec[trough_en[2] - 1]:
                trough_en[2] += 1
            total_volume[2] += _integrate_trough(vec, trough_st[2], trough_en[2])
            trough_st[2] = trough_en[2] - 1
        trough_en[0] += 1
        trough_en[1] -= 1
        trough_en[2] += 1
    print(f"volume: {total_volume}")
    return max(total_volume)


if __name__ == "__main__":
    assert integrate([2, 1, 2]) == 1
    assert integrate([3, 0, 1, 3, 0, 5]) == 8

    assert integrate([]) == 0
    assert integrate([1]) == 0
    assert integrate([10, 1]) == 0
    assert integrate([10, 100]) == 0

    assert integrate([1, 2, 3, 4, 5]) == 0
    assert integrate([5, 4, 3, 2, 1]) == 0
    assert integrate([5, 4, 3, 2, 1, 2, 3, 4, 5]) == 16
    assert integrate([2, 1, 2, 1, 2, 1]) == 2
    assert integrate([2, 1, 2, 1, 2, 1, 2]) == 3

    assert integrate([10, 2, 1, 3, 1, 2, 1, 10]) == 50
    assert integrate([10, 2, 1, 3, 1, 2, 1]) == 4
    assert integrate([10, 2, 1, 3, 1, 2, 1, 9]) == 44
    assert integrate([10, 2, 1, 3, 1, 2, 1, 9, 2, 1, 3, 1, 2, 1, 9]) == 88
    assert integrate([10, 2, 1, 3, 1, 2, 1, 8, 2, 1, 3, 1, 2, 1, 9]) == 89
    assert integrate([10, 2, 1, 3, 1, 2, 1, 9, 2, 1, 3, 1, 2, 1, 10]) == 101
