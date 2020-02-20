"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of
its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

* `is_locked`, which returns whether the node is locked
* `lock`, which attempts to lock the node. If it cannot be locked, then it should return false.
  Otherwise, it should lock it and return true.
* `unlock`, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise,
it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for actual locks
or mutexes. Each method should run in O(h), where h is the height of the tree.
TODO
This is still O(2^h) not O(h).
"""
from operator import or_, and_
from functools import reduce
from typing import List
Vector = List[bool]


class Node:
    def __init__(self, name: str, locked: bool, left_node=None, right_node=None, parent_node=None):
        self.name = name
        self.locked: bool = locked
        self.parent: Node = parent_node
        self.left: Node = left_node
        self.right: Node = right_node
        self.locked_descendant = False
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def _traverse_ante(root: Node, node_func, combine_func):
    """
    Traverse the antecedents of the given node, applying node_func, and
    then using combine_func to merge all results of applying node_func.
    """
    if root is None:
        return False
    parent = root.parent
    locked = list()
    while parent is not None:
        locked.append(node_func(parent))
        parent = parent.parent
    if not locked:
        return False
    return combine_func(locked)


def _traverse_desc(root: Node, node_func, combine_func, include_self: bool = True):
    """
    Traverse the descendants of the given node, applying node_func, and
    then using combine_func to merge all results of applying node_func.
    """
    if root is None:
        return False
    locked = list()
    locked_p = False
    locked_l = False
    locked_r = False
    if include_self:
        locked_p = node_func(root)
    if root.left is not None:
        locked_l = _traverse_desc(root.left, node_func, combine_func)
    if root.right is not None:
        locked_r = _traverse_desc(root.right, node_func, combine_func)
    locked.extend([locked_p, locked_l, locked_r])
    if not locked:
        return False
    return combine_func(locked)


def is_locked(root: Node, include_self: bool = True) -> bool:
    def _node_is_locked(node: Node):
        return node.locked

    def _combine_is_locked(vec: Vector):
        return reduce(or_, vec)

    a = _traverse_ante(root, _node_is_locked, _combine_is_locked)
    d = _traverse_desc(root, _node_is_locked, _combine_is_locked, include_self)
    return _combine_is_locked([a, d])


def lock(root: Node) -> bool:
    if not root:
        return False
    if is_locked(root, False):
        return False

    def _node_lock(node: Node):
        if not node.locked:
            node.locked_antecedent = True
            return True
        return False

    def _combine_lock(vec: Vector):
        return True

    root.locked = True
    return _traverse_desc(root, _node_lock, _combine_lock, False)


def unlock(root: Node) -> bool:
    if not root:
        return False
    if is_locked(root, False):
        return False

    def _node_unlock(node: Node):
        if not node.locked:
            node.locked = False
            return True
        return False

    def _combine_unlock(vec: Vector):
        return True

    root.locked = False
    return _traverse_desc(root, _node_unlock, _combine_unlock, False)


if __name__ == "__main__":
    T = True
    F = False
    root = Node('a', F,
                Node('b', F,
                     Node('d', F,
                          Node('f', F), Node('h', F))),
                Node('c', F,
                     Node('e', F,
                          Node('g', F), Node('i', F))))

    assert is_locked(root) is False
    assert lock(root) is True
    assert unlock(root) is True

    assert lock(root.left.left.left) is True
    assert unlock(root) is False
