"""
Implement a stack that has the following methods:

* push(val), which pushes an element onto the stack
* pop(), which pops off and returns the topmost element of the stack. If there are no elements
  in the stack, then it should throw an error or return null.
* max(), which returns the maximum value in the stack currently. If there are no elements in
  the stack, then it should throw an error or return null.

Each method should run in constant time.
"""
from typing import List
Vector = List[int]


class Stack:
    def __init__(self):
        self.data = list()
        self.max_elem = None

    def len(self):
        return len(self.data)

    def push(self, item):
        self.data.append(item)
        if self.max_elem is None or item > self.max_elem:
            self.max_elem = item
        return self

    def pop(self):
        if self.len() == 0:
            return None
        result = self.data[self.len() - 1]
        self.data.remove(result)
        # Not sure how to do this in O(1)
        self.max_elem = None if self.len() == 0 else max(self.data)
        return result

    def max(self):
        if self.len() == 0:
            return None
        return self.max_elem;


if __name__ == "__main__":
    stack = Stack()
    stack.push(3).push(2).push(1)

    assert stack.max() == 3
    assert stack.pop() == 1
    assert stack.max() == 3
    assert stack.pop() == 2
    assert stack.max() == 3
    assert stack.pop() == 3
