"""
Suppose we represent our file system by a string in the following manner:

The string "`dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext`" represents:
```
dir
    subdir1
    subdir2
        file.ext
```
The directory dir contains an empty sub-directory `subdir1` and a sub-directory `subdir2`
containing a file `file.ext`.

The string "`dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext`"
represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
The directory dir contains two sub-directories `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext`
and an empty second-level sub-directory `subsubdir1`. `subdir2` contains a second-level sub-directory
`subsubdir2` containing a file `file2.ext`.

We are interested in finding the longest (number of characters) absolute path to a file within our
file system. For example, in the second example above, the longest absolute path is
"`dir/subdir2/subsubdir2/file2.ext`", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest
absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""


class Node:
    def __init__(self, name, parent, children: set, is_file: bool):
        self.name = name
        self.parent = parent
        self.children = children
        self.is_file = is_file

    def find_or_create(self, name, is_file: bool):
        for child in self.children:
            if name == child.name:
                return child
        return Node(name, self, set(), is_file)

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other


class FileSystemUtils:
    @staticmethod
    def _is_file(name: str):
        return name.find(".") >= 0

    @staticmethod
    def _find_depth(name: str):
        return name.count("\t")

    @staticmethod
    def _find_parent(line_num, prev, depth_diff):
        if depth_diff == 1:
            return prev
        elif depth_diff == 0:
            return prev.parent
        elif depth_diff < 0:
            dist = depth_diff
            parent = prev.parent
            while dist < 0:
                parent = parent.parent
                dist = dist + 1
            return parent
        raise ValueError(f"Filesystem read error at line {line_num}")

    @staticmethod
    def _make_tree_node(line, line_num, prev_depth, prev_node):
        depth = FileSystemUtils._find_depth(line)
        depth_diff = depth - prev_depth
        parent = FileSystemUtils._find_parent(line_num, prev_node, depth_diff)
        node_name = line.strip("\t")
        is_file = FileSystemUtils._is_file(line)
        node: Node = parent.find_or_create(node_name, is_file)
        parent.children.add(node)
        return node, depth, line_num + 1

    @staticmethod
    def make_tree(data: str, root_name: str = ""):
        root: Node = Node(root_name, None, set(), False)
        prev_node = root
        prev_depth = -1
        line_num = 1
        for line in data.split("\n"):
            assert line
            prev_node, prev_depth, line_num = \
                FileSystemUtils._make_tree_node(line, line_num, prev_depth, prev_node)
        return root

    @staticmethod
    def _find_longest_path(node: Node):
        if not node:
            return False, ""
        if not node.children:
            return node.is_file, node.name
        has_file = False
        file_path = ""
        for child in node.children:
            has_file_in_subtree, file_path_in_subtree = FileSystemUtils._find_longest_path(child)
            has_file = has_file | has_file_in_subtree
            if has_file_in_subtree:
                path = node.name + "/" + file_path_in_subtree
                file_path = path if len(path) > len(file_path) else file_path
        return has_file, file_path

    @staticmethod
    def find_longest_path(data: str):
        root_name = ""
        root: Node = FileSystemUtils.make_tree(data, root_name)
        has_file, file_path = FileSystemUtils._find_longest_path(root)
        if not has_file:
            return 0
        # decremented since the path name starts with a super-root
        return len(file_path) - 1 - len(root_name)


if __name__ == "__main__":
    result = FileSystemUtils.find_longest_path("dir\n\tsubdir1\n\tsubdir2")
    assert result == 0

    result = FileSystemUtils.find_longest_path("abc.pdf")
    assert result == 7

    result = FileSystemUtils.find_longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    assert result == 20

    result = FileSystemUtils.find_longest_path(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    assert result == 32
