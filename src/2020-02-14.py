"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
from functools import cmp_to_key
from typing import List, Tuple
Pair = Tuple[int, int]
Ranges = List[Pair]


def compare_ranges(r1: Pair, r2: Pair) -> int:
    if r1[0] == r2[0]:
        return r1[1] - r2[1]
    if r1[0] < r2[0]:
        return -1
    return 1


def do_ranges_intersect(r1: Pair, r2: Pair) -> bool:
    if not r1 or not r2:
        return False
    if r1[0] == r2[0] or r1[1] == r2[1]:
        return True
    earlier = r2
    later = r1
    if r1[0] < r2[0]:
        earlier = r1
        later = r2
    if earlier[1] > later[0]:
        return True
    return False


def get_range_intersection(r1: Pair, r2: Pair) -> Pair:
    earlier = r2
    later = r1
    if r1[0] < r2[0]:
        earlier = r1
        later = r2
    return max(earlier[0], later[0]), min(earlier[1], later[1])


def get_max_rooms(ranges: Ranges) -> int:
    if not ranges:
        return 0
    sorted_ranges = sorted(ranges, key=cmp_to_key(compare_ranges))
    max_isect_count = 1
    isect_count = 1
    isection = None
    last_range = sorted_ranges[0]
    for range in sorted_ranges[1:]:
        if do_ranges_intersect(isection, range):
            isection = get_range_intersection(isection, range)
            isect_count = isect_count + 1
        elif do_ranges_intersect(last_range, range):
            isection = get_range_intersection(last_range, range)
            isect_count = 2
        else:
            isection = None
            isect_count = 1
        max_isect_count = max(max_isect_count, isect_count)
    return max_isect_count


if __name__ == "__main__":
    assert get_max_rooms([]) == 0
    assert get_max_rooms([(0, 1)]) == 1
    assert get_max_rooms([(55, 75), (0, 50), (76, 150)]) == 1
    assert get_max_rooms([(30, 75), (0, 50), (60, 150)]) == 2
    assert get_max_rooms([(30, 75), (0, 50), (40, 150)]) == 3
    assert get_max_rooms([(30, 75), (0, 50), (40, 150), (100, 150), (140, 200)]) == 3
    assert get_max_rooms([(30, 75), (0, 50), (40, 150), (47, 150), (46, 200)]) == 5
