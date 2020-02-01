"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next
and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an `add(element)` which adds the element to the end, and a
`get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to
`get_pointer` and `dereference_pointer` functions that converts between nodes and memory addresses.

0 ^ 1, 1 ^ 2, 2 ^ 3, ... (n-1) ^ 0
"""


class LinkedList:
    class Node:
        def __init__(self, both, val):
            self.both = both
            self.val = val

    def __init__(self):
        self.memory = list()
        self.len = 0

    def add(self, element):
        node = LinkedList.Node(self.len, element)
        if self.len > 0:
            tail_node = self.get(self.len - 1)
            tail_node.both = tail_node.both ^ node.both
        self.memory.append(node)
        self.len = self.len + 1
        return self

    def get(self, index):
        """
        :param index: [0 .. len-1]
        :return: node at given index
        """
        if self.len == 0:
            return None
        if index == self.len - 1:
            return self.dereference_pointer(index)
        tail_addr = 0
        tail_node = self.dereference_pointer(tail_addr)

        for idx in range(index):
            tail_addr = tail_addr ^ tail_node.both
            tail_node = self.dereference_pointer(tail_addr)
        return tail_node

    def dereference_pointer(self, addr):
        return self.memory[addr]


if __name__ == "__main__":
    ll = LinkedList()
    for idx in range(10):
        ll.add(idx * 11)
    for idx in range(10):
        assert ll.get(idx).val == idx * 11
