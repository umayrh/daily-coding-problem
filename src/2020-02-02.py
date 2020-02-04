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
    This solution is based on Jen Haskell's pseudocode.
    :param vec: list of integers
    :return: largest sum of non-adjacent numbers
    """
    if not vec:
        return 0
    last_pos_idx = -1
    val_last_pos = 0

    for idx in range(len(vec)):
        if vec[idx] > 0:
            val_idx_minus2 = vec[idx - 2] if idx - 2 >= 0 and vec[idx - 2] >= 0 else 0
            val_idx_minus3 = vec[idx - 3] if idx - 3 >= 0 and vec[idx - 3] >= 0 else 0
            vec[idx] = max(val_idx_minus2, val_idx_minus3, val_last_pos) + vec[idx]
        last_pos_idx = idx - 1 if idx - 1 >= 0 and vec[idx - 1] > val_last_pos else last_pos_idx
        val_last_pos = vec[last_pos_idx] if last_pos_idx > 0 else val_last_pos
    return max(max(vec), 0)


if __name__ == "__main__":
    assert sum_nonadjacent([2]) == 2
    assert sum_nonadjacent([0]) == 0
    assert sum_nonadjacent([-1]) == 0

    assert sum_nonadjacent([-1, 0, 0]) == 0
    assert sum_nonadjacent([-1, 0, 1]) == 1

    assert sum_nonadjacent([2, 4, 6, 2, 5]) == 13
    assert sum_nonadjacent([5, 1, 1, 5]) == 10
    assert sum_nonadjacent([20, 23, 10]) == 30
    assert sum_nonadjacent([2, -4, 6, -2, 5]) == 13
    assert sum_nonadjacent([-1, -9, 2, -4, -4, 0, 1, 0, 0, -2, 5]) == 8
    assert sum_nonadjacent([-5, -3, 0, 8, 2, 0, -1, 0, 0, -2, 5]) == 13
