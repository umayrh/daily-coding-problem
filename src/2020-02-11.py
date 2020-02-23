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
import heapq
from typing import List
Vector = List[int]


def subset_max(vec: Vector, k: int):
    if not vec:
        return vec
    max_heap = []
    k_list = list()
    idx = 0
    for item in vec:
        new_node = [-item, idx]
        if idx >= k:
            removed_node = k_list[idx % k]
            k_list[idx % k] = new_node
            removed_node[0] = new_node[0]
            removed_node[1] = new_node[1]
            heapq.heapify(max_heap)
            vec[idx - k + 1] = -max_heap[0][0]
        else:
            k_list.append(new_node)
            heapq.heappush(max_heap, new_node)
            if idx == k - 1:
                vec[0] = -max_heap[0][0]
        idx = idx + 1
    return vec[0:len(vec) - k + 1]


if __name__ == "__main__":
    assert subset_max([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
