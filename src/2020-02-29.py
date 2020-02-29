"""
Given the root to a binary search tree, find the second largest node in the tree.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def second_max(root: Node):
    # No self
    if root is None:
        return None
    # No children
    if root.right is None and root.left is None:
        return None
    # No grandchildren
    if root.left or root.right:
        has_left_grandkids = root.left and (root.left.left or root.left.right)
        has_right_grandkids = root.right and (root.right.left or root.right.right)
        if not has_left_grandkids and not has_right_grandkids:
            return root
    node = root.right
    parent = root
    grandparent = None
    # Right most's first left
    while node is not None:
        grandparent = parent
        parent = node
        node = node.right
    if parent.left is None:
        return grandparent
    # Or first left's right most
    node = parent.left
    while node is not None:
        parent = node
        node = node.right
    return parent


if __name__ == "__main__":
    assert second_max(Node(2, Node(1), Node(3))).val == 2
    assert second_max(Node(2, Node(1))).val == 2
    assert second_max(Node(2, None, Node(3))).val == 2

    tree = Node(8, Node(3, Node(1), Node(4, Node(6), Node(7))), Node(10, None, Node(14, Node(13))))
    assert second_max(tree).val == 13, second_max(tree).val

    subtree = Node(7, Node(2), Node(32, Node(24), Node(37, None, Node(40))))
    tree = Node(120, Node(42, Node(42, subtree)))
    assert second_max(tree).val == 42, second_max(tree).val

    tree = Node(37, Node(24, Node(7, Node(2)), Node(32)), Node(42, Node(42, Node(40)), Node(120)))
    assert second_max(tree).val == 42, second_max(tree).val

    tree = Node(20, Node(2, None, Node(5, None, Node(7, None, Node(10)))))
    assert second_max(tree).val == 10, second_max(tree).val
