"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum
values of each subarray of length k.

For example, given array = `[10, 5, 2, 7, 8, 7]` and k = 3, we should get: `[10, 7, 8, 8]`, since:
```
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
```
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need
to store the results. You can simply print them out as you compute them.
TODO
"""
from random import randint
from typing import List
Vector = List[int]


def _swap(vec: Vector, i: int, j: int):
    val = vec[i]
    vec[i] = vec[j]
    vec[j] = val


def _partition(vec: Vector, st_idx: int, en_idx: int, pivot_val: int):
    """
    _partition([1, 2, 5, 4, 3], 0, 3, 3)
      [1, 2, 5, 4, 3]
      [4, 2, 5, 1, 3]
      [4, 5, 2, 1, 3]
    :param vec: vector of comparables
    :param st_idx: start index (inclusive)
    :param en_idx: end index (inclusive)
    :param pivot_val: pivot value (used for comparison)
    :return: the appropriate index for pivot_val
    """
    i = st_idx
    j = en_idx
    print(f"i {i}, j {j}: {vec}")
    while i < j and i <= en_idx and j >= st_idx:
        while vec[i] > pivot_val:
            i = i + 1
        while vec[j] < pivot_val:
            j = j - 1
        if vec[i] < pivot_val < vec[j]:
            _swap(vec, i, j)
        i = i + 1
        print(f"i {i}, j {j}: {vec}")
    return j


def _quick_select(vec: Vector, k: int = 0):
    """
    Returns the k-th maximum value in the given vector in O(n) amortized time.
    :param vec: vector of comparable
    :param k: order of the max value
    :return: the k-th max value in the index
    1 2 3 4 5
    1 2 5 4 3
    4 2 5 1 3
    4 5 2 1 3
    """
    vec_len = len(vec)
    if vec_len <= 3:
        return sorted(vec, reverse=True)[k]

    en_idx = vec_len
    while en_idx > 2:
        pivot_idx = randint(0, en_idx - 1)
        pivot_val = vec[pivot_idx]
        _swap(vec, 0, pivot_idx)
        pivot_idx_new = _partition(vec, 1, en_idx - 1, pivot_val)
        _swap(vec, 0, pivot_idx_new)
        en_idx = pivot_idx_new
        print(f"pivot {pivot_idx}, pivot_val {pivot_val}, new_idx {pivot_idx_new}: {vec}")
    return vec[0]


def subset_max(vec: Vector, k: int):
    """
    :param k:
    :param vec:
    :return:
    """
    if not vec:
        return vec
    max_list: Vector = list()
    last_max = vec[0]
    count = 0
    for item in vec:
        if count < k:
            max_list.append(item)
            last_max = max(item, last_max)
        else:
            removed = max_list[count % k]
            if removed == last_max:
                pass
            max_list[count % k] = item
        count = count + 1
    pass


if __name__ == "__main__":
    # print(subset_max([10, 5, 2, 7, 8, 7], 3))
    _partition([5, 2, 3, 4, 1], 1, 4, 5)
    _partition([3, 2, 1, 4, 5], 1, 4, 3)
    # _quick_select([1, 2, 5, 4, 3])
    pass
