"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give 2. The input `[1, 2, 0]` should give 3.

You can modify the input array in-place.
"""
import sys
from typing import List
Vector = List[int]


def find_missing_int(vec: Vector):
    """
    map the sequence to 0...LEN-1
       set neg values to 0
       how to deal with neg values? bubble to the end?
       find min, max, and length of array
    if sorted, with all negs set to 0:
       if pairwise difference in seq <= 1
         return max(seq) + 1
       else
         return min(pair) + 1
    TODO this surely can be simplified
    :param vec: list of integers
    :return: lowest integer not in the list
    """
    if not vec:
        return 1
    input_len = len(vec)
    min_val = sys.maxsize
    max_val = - sys.maxsize - 1
    for item in vec:
        if 0 <= item > max_val:
            max_val = item
        if 0 <= item < min_val:
            min_val = item
    if sys.maxsize == min_val or min_val > 1:
        return 1
    if min_val == max_val:
        if min_val == 1:
            return 2
        else:
            return 1
    for idx in range(input_len):
        vec[idx] = vec[idx] - min_val if vec[idx] > 0 else 0

    for idx in range(input_len):
        # try to map the sequence to natural numbers: offset by min_val
        item = vec[idx]
        new_val = item - min_val if item > 0 else item
        # swap till idx find its corresponding value (which is min_val for idx 0)
        while input_len > new_val != idx and vec[idx] != vec[new_val]:
            _swap(vec, idx, new_val)
            new_val = vec[idx] - min_val if item > 0 else item
    for idx in range(input_len - 1):
        # find a gap
        if vec[idx] < vec[idx + 1] - 1:
            return vec[idx] + min_val + 1
    # only if all values in the list could be mapped to a continuous sequence of natural numbers
    return max_val + 1


def _swap(arr: Vector, curr_idx: int, new_idx: int):
    val = arr[curr_idx]
    arr[curr_idx] = arr[new_idx]
    arr[new_idx] = val


if __name__ == "__main__":
    assert find_missing_int([3, 4, -1, 1]) == 2
    assert find_missing_int([1, 2, 0]) == 3
    assert find_missing_int([1, 2, 0, 6, 5, 4, 8, 10, 9]) == 3
    assert find_missing_int([3, 1, 2, 0, 6, 5, 4, 8, 10, 9]) == 7
    assert find_missing_int([1, 1, 1, 1]) == 2
    assert find_missing_int([10, 100, 10000, 100000]) == 1
