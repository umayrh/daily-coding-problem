"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean
represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
required to reach the end coordinate from the start. If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the
edges of the board.

For example, given the following board:
```
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
```
and start = `(3, 0)` (bottom left) and end =` (0, 0)` (top left), the minimum number of steps required
to reach the end is 7, since we would need to go through `(1, 2)` because there is a wall everywhere
else on the second row.
"""
import sys
from typing import List, Tuple
Matrix = List[List[int]]
Pair = Tuple[int, int]


def _outside(matrix: Matrix, st: Pair) -> bool:
    if st[0] < 0 or st[1] < 0 or st[1] >= len(matrix) or st[0] >= len(matrix[0]):
        return True
    return False


def _min_maze_steps(matrix: Matrix, path: set, st: Pair, en: Pair) -> int:
    if st == en:
        return 0
    if _outside(matrix, st):
        return -1
    min_steps = sys.maxsize
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        a, b = st[0] + x, st[1] + y
        if not _outside(matrix, (a, b)) and not (a, b) in path and not matrix[a][b]:
            next_min_steps = _min_maze_steps(matrix, path.union({(a, b)}), (a, b), en)
            if next_min_steps >= 0:
                min_steps = min(min_steps, next_min_steps + 1)
    return min_steps if min_steps != sys.maxsize else -1


def min_maze_steps(matrix: Matrix, st: Pair, en: Pair) -> int:
    if not matrix:
        return None
    result = _min_maze_steps(matrix, {st}, st, en)
    if result < 0:
        return None
    return result


if __name__ == "__main__":
    t = True
    f = False
    maze = [[f, f, f, f],
            [t, t, f, t],
            [f, f, f, f],
            [f, f, f, f]]
    result = min_maze_steps(maze, (3, 0), (0, 0))
    assert result == 7, result
