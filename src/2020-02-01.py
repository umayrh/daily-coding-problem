"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```
"""


class Node:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

    @staticmethod
    def leaf(val):
        return Node(None, None, val)


def count_subtrees(root: Node):
    """
    :param root: root to a binary tree
    :return: number of unival subtrees
    """
    val, count, is_unival = _count_subtrees(root, 0)
    return count


def _count_subtrees(node: Node, parent_val):
    if not node:
        return parent_val, 0, True
    left_val, left_count, is_left_unival = _count_subtrees(node.left, node.val)
    right_val, right_count, is_right_unival = _count_subtrees(node.right, node.val)
    is_unival = is_left_unival and is_right_unival and left_val == node.val == right_val
    count = left_count + right_count
    if is_unival:
        count = count + 1
    return node.val, count, is_unival


if __name__ == "__main__":
    t1 = Node(Node.leaf(1), Node.leaf(1), 1)
    t2 = Node(t1, Node.leaf(0), 0)
    t3 = Node(Node.leaf(1), t2, 0)
    assert count_subtrees(t3) == 5

    t1 = Node(Node.leaf(1), Node.leaf(1), 1)
    t2 = Node(t1, Node.leaf(1), 1)
    t3 = Node(Node.leaf(1), t2, 1)
    assert count_subtrees(t3) == 7
