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
from typing import Dict, List, Tuple
Matrix = List[List[int]]
Pair = Tuple[int, int]
Cache = Dict[Pair, int]


def _outside(matrix: Matrix, st: Pair) -> bool:
    if st[0] < 0 or st[1] < 0 or st[1] >= len(matrix) or st[0] >= len(matrix[0]):
        return True
    return False


def _min_maze_steps(matrix: Matrix, path: set, st: Pair, en: Pair, cache: Cache) -> int:
    if st in cache:
        return cache[st]
    if st == en:
        cache[st] = 0
        return 0
    if _outside(matrix, st):
        cache[st] = -1
        return -1
    min_steps = sys.maxsize
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        a, b = st[0] + x, st[1] + y
        if not _outside(matrix, (a, b)) and not matrix[a][b] and not (a, b) in path:
            new_path = path.union({(a, b)})
            next_min_steps = _min_maze_steps(matrix, new_path, (a, b), en, cache)
            if next_min_steps >= 0:
                min_steps = min(min_steps, next_min_steps + 1)
    result = min_steps if min_steps != sys.maxsize else -1
    cache[st] = result
    return result


def min_maze_steps(matrix: Matrix, st: Pair, en: Pair) -> int:
    if not matrix:
        return None
    cache: Cache = {}
    result = _min_maze_steps(matrix, {st}, st, en, cache)
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

    result = min_maze_steps(maze, (0, 0), (0, 2))
    assert result == 2, result

    result = min_maze_steps(maze, (0, 0), (2, 0))
    assert result == 6, result
