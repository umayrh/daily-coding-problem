"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and
deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:

```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(tree: Node):
    code = list()
    _serialize(tree, 1, code)
    return '|'.join(code)


def _serialize(root: Node, level: int, code: list):
    if root.left:
        _serialize(root.left, level << 1, code)

    code.append(str(level))
    code.append(root.val)

    if root.right:
        _serialize(root.right, (level << 1) + 1, code)


def deserialize(tree_str: str):
    code = tree_str.split('|')
    root: Node = Node(None, None, None)

    for idx in range(0, len(code), 2):
        _deserialize(root, int(code[idx]), code[idx+1])
    return root


def _deserialize(root: Node, addr_int: int, val: str):
    # root is the most significant bit
    current: Node = Node(None, None, root)
    previous: Node = root

    for bit in "{0:b}".format(addr_int):
        previous = current
        if bit == '1':
            current = current.right
            if not current:
                current = Node(None, None, None)
                previous.right = current
        else:
            current = current.left
            if not current:
                current = Node(None, None, None)
                previous.left = current
    current.val = val


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
