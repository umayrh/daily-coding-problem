"""
Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node:
    def __init__(self, val: int, next_node=None):
        self.next = next_node
        self.val = val


def remove(head: Node, k: int) -> Node:
    count = 0
    next_node = head
    rem_node = head
    while next_node is not None:
        if count >= k:
            rem_node = rem_node.next
        next_node = next_node.next
        count = count + 1
    return rem_node


if __name__ == "__main__":
    ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert remove(ll, 2).val == 4

    assert remove(Node(1, Node(2)), 2).val == 1
    assert remove(Node(1, Node(2)), 1).val == 2
