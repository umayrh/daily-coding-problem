"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
write a function that returns the number of unique ways you can climb the staircase. The order of the
steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set
of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

from typing import List, Dict
Vector = List[int]
Map = Dict[int, int]


def count_stairs(strides: Vector, steps: int):
    if not strides or steps <= 0:
        return 0
    cache = {}
    return _count_stairs(strides, steps, cache)


def _count_stairs(strides: Vector, steps: int, cache: Map = {}):
    if steps <= 0:
        return 0
    total_count = 0
    if steps in cache:
        return cache[steps]
    elif steps in strides:
        total_count = 1
    for stride in strides:
        total_count += _count_stairs(strides, steps - stride, cache)
    cache[steps] = total_count
    return total_count


if __name__ == "__main__":
    assert count_stairs([1, 2], 1) == 1
    assert count_stairs([1, 2], 2) == 2
    assert count_stairs([1, 2], 4) == 5
    assert count_stairs([1, 3, 5], 5) == 5
