"""
Given a list of integers S and a target number k, write a function that returns a subset of S
that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
from typing import List
Vector = List[int]


def _subset_sum(vec: Vector, k: int, st: int) -> Vector:
    if not vec or st >= len(vec):
        return None
    if st >= len(vec) - 2:
        if k in vec[st:]:
            return [k]
        if sum(vec[st:]) == k:
            return vec[st:]
        return None
    res = _subset_sum(vec, k - vec[st], st+1)
    if res:
        res.append(vec[st])
    else:
        res = _subset_sum(vec, k, st+1)
    return res


def subset_sum(vec: Vector, k: int) -> Vector:
    return _subset_sum(vec, k, 0)


if __name__ == "__main__":
    result = subset_sum([12, 1, 61, 5, 9, 2], 24)
    assert set(result) == {12, 9, 2, 1}
    result = subset_sum([0, 0, 1, 2, 9, 8], 17)
    assert set(result) == {9, 8, 0, 0}
    result = subset_sum([10, 1000, 1, 2, 9, 8], 222)
    assert result is None
