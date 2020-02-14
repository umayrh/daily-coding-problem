"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node


def _len(v: Node) -> int:
    st: Node = v
    len_v = 0
    while st is not None:
        len_v = len_v + 1
        st = st.next
    return len_v


def do_lists_intersect(list1: Node, list2: Node) -> Node:
    if not list1 or not list2:
        return None
    if list1 == list2:
        return list1
    len1 = _len(list1)
    len2 = _len(list2)

    longer_list = list1 if len1 > len2 else list2
    len_diff = max(len2, len1) - min(len2, len1)

    st: Node = longer_list
    for idx in range(len_diff):
        st = st.next

    shorter_list = list1 if longer_list == list2 else list2
    for idx in range(min(len1, len2)):
        if shorter_list == st:
            return st
        st = st.next
        shorter_list = shorter_list.next
    return None


if __name__ == "__main__":
    c = Node(8, Node(10))
    a = Node(3, Node(7, c))
    b = Node(99, Node(1, c))
    assert do_lists_intersect(a, b) == c

    a = Node(3, Node(7))
    b = Node(99, Node(1))
    assert do_lists_intersect(a, b) is None

    c = Node(8, Node(10))
    a = Node(3, Node(7, c))
    b = Node(99, Node(1, Node(23, Node(46, Node(87, c)))))
    assert do_lists_intersect(a, b) == c
