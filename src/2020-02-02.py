"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, `[2, 4, 6, 2, 5]` should return 13, since we pick 2, 6, and 5. `[5, 1, 1, 5]` should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
from typing import List
Vector = List[int]


def sum_nonadjacent(vec: Vector):
    """
    :param vec: list of integers
    :return: largest sum of non-adjacent numbers
    """
    if not vec:
        return 0
    vec_len = len(vec)
    max_val = 0
    max_idx = -1
    for idx in range(vec_len):
        if max_val > vec[idx]:
            max_val = vec[idx]
            max_idx = idx
    # max val is a good place to start to construct two sequences:
    # one including max_val, and another including the max of values adjacent to max_val.
    # Each sequence is composed of two subsequences: one with idx increasing, the other decreasing.
    max_seq_sum = max_val
    for idx in range(max_idx + 2, vec_len, 1):
        # for each non-adjacent, decide whether to use it or its neighbor
        # ...
        if max_seq_sum > max_seq_sum + vec[idx]:
            max_seq_sum = max_seq_sum + vec[idx]
    for idx in range(0, max_idx - 1, 1):
        if max_seq_sum > max_seq_sum + vec[idx]:
            max_seq_sum = max_seq_sum + vec[idx]
    # second sequence


if __name__ == "__main__":
    assert sum_nonadjacent([2, 4, 6, 2, 5]) == 13
    assert sum_nonadjacent([5, 1, 1, 5]) == 10
    assert sum_nonadjacent([20, 23, 10]) == 30
