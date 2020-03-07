"""
Given an unordered list of flights taken by someone, each represented as (origin, destination)
pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists,
return null. If there are multiple possible itineraries, return the lexicographically
smallest one. All flights must be used in the itinerary.

For example, given the list of flights `[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'),
('HKO', 'ORD')]` and starting airport 'YUL', you should return the list
`['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']`.

Given the list of flights `[('SFO', 'COM'), ('COM', 'YYZ')]` and starting airport 'COM', you
should return null.

Given the list of flights `[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]` and starting
airport 'A', you should return the list `['A', 'B', 'C', 'A', 'C']` even though
`['A', 'C', 'A', 'B', 'C']` is also a valid itinerary. However, the first one is
lexicographically smaller.
"""
from typing import List, Set, Tuple
import heapq


class Node:
    def __init__(self, val: str):
        self.val = val
        self.next_nodes: list = []


StrVector = List[str]
NodeVector = List[Node]
PairSet = Set[Tuple[str, str]]


def topological_sort(vec: PairSet, st: str) -> StrVector:
    nodes = {}
    for src, dst in vec:
        if dst not in nodes:
            nodes[dst] = Node(dst)
        if src not in nodes:
            nodes[src] = Node(src)
        heapq.heappush(nodes[src].next_nodes, dst)
    if st not in nodes or not nodes[st].next_nodes:
        return None
    dst = heapq.heappop(nodes[st].next_nodes)
    stack = [(st, dst)]
    path = []
    while len(stack) > 0:
        src, dst = stack.pop()
        path.append(src)
        if len(nodes[dst].next_nodes) > 0:
            src = dst
            dst = heapq.heappop(nodes[src].next_nodes)
            stack.append((src, dst))
        elif len(set(path).union([dst])) == len(nodes):
            path.append(dst)
        else:
            # dead-end path
            path.pop()
    print(f"path: {path}")
    return path if len(path) > 0 and len(set(path)) == len(nodes) else None


if __name__ == "__main__":
    result = topological_sort({('SFO', 'COM'), ('COM', 'YYZ')}, 'COM')
    assert result is None
    result = topological_sort({('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')}, 'YUL')
    assert result == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    result = topological_sort({('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')}, 'A')
    assert result == ['A', 'B', 'C', 'A', 'C']
