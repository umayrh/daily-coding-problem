"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all
the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array `['G', 'B', 'R', 'R', 'B', 'R', 'G']`, it should become
`['R', 'R', 'R', 'G', 'G', 'B', 'B']`.
"""
from typing import List
Vector = List[chr]


def domain_sort(vec: Vector) -> Vector:
    if not vec:
        return vec
    domain_count = {'R': 0, 'G': 0, 'B': 0}
    for char in vec:
        domain_count[char] += 1
    for idx in range(len(vec)):
        out = ''
        if domain_count['R'] > 0:
            out = 'R'
        elif domain_count['G'] > 0:
            out = 'G'
        elif domain_count['B'] > 0:
            out = 'B'
        vec[idx] = out
        domain_count[out] -= 1
    return vec


if __name__ == "__main__":
    assert domain_sort(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
