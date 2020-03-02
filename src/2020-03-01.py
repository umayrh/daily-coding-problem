"""
The power set of a set is the set of all its subsets. Write a function that, given a set,
generates its power set.

For example, given the set `{1, 2, 3}`, it should return `{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}`
"""
from math import pow


def power_set(s: set) -> set:
    if not s:
        return frozenset()
    size = len(s)
    elem = list(s)
    powerset = list()
    for code in range(int(pow(2, size))):
        subset = set()
        for idx in range(size):
            if code & 1:
                subset.add(elem[idx])
            code = code >> 1
        powerset.append(frozenset(subset))
    return frozenset(powerset)


if __name__ == "__main__":
    assert power_set({1, 2, 3}) == frozenset([frozenset(), frozenset({1}), frozenset({2}), frozenset({3}),
                                              frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3}),
                                              frozenset({1, 2, 3})])
