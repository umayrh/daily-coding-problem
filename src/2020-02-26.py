"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
```
2
1.5
2
3.5
2
2
2
```
"""
import heapq
from typing import List
Vector = List[int]


def running_median(item: int, heap) -> int:
    heapq.heappush(heap, item)
    size = len(heap)
    middle_idx = int(size/2) + 1
    if size % 2 == 0:
        return sum(heapq.nsmallest(middle_idx, heap)[-2:]) / 2
    return heapq.nsmallest(middle_idx, heap)[-1]


if __name__ == "__main__":
    expected = [2, 1.5, 2, 3.5, 2, 2, 2]
    heap = []
    for idx, item in enumerate([2, 1, 5, 7, 2, 0, 5]):
        result = running_median(item, heap)
        assert result == expected[idx], f"{idx}, {item}, {result}"
