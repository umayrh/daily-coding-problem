"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each
cell is either dead or alive, and at each tick, the following rules apply:

* Any live cell with less than two live neighbours dies.
* Any live cell with two or three live neighbours remains living.
* Any live cell with more than three live neighbours dies.
* Any dead cell with exactly three live neighbours becomes a live cell.
* A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of
live cell coordinates and the number of steps it should run for. Once initialized, it should
print out the board state at each step. Since it's an infinite board, print out only the
relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (`*`) and a dead cell with a dot (`.`).
"""
from typing import List, Tuple
Matrix = List[List[int]]
Vector = List[Tuple]


def print_board(board: Matrix, step: int, print_all=False):
    rows = len(board)
    cols = len(board[0])
    top_left = rows, cols
    bottom_right = rows, cols
    if print_all:
        top_left = 0, 0
        bottom_right = rows, cols
    else:
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    if top_left == (rows, cols):
                        top_left = row, col
                    bottom_right = row, col
    col_en = max(top_left[1], bottom_right[1])
    print(step)
    for row in range(top_left[0], rows):
        line = ""
        for col in range(col_en):
            line += "*\t" if board[row][col] > 0 else ".\t"
        print(f"{line}\n")


def neighbors(board_size, cell: Tuple) -> Vector:
    row = cell[0]
    col = cell[1]
    st_row = row - 1 if row > 0 else 0
    en_row = row + 1 if row < board_size - 1 else board_size - 1
    st_col = col - 1 if col > 0 else 0
    en_col = col + 1 if col < board_size - 1 else board_size - 1
    my_neighbors: Vector = []
    for r in range(st_row, en_row + 1):
        for c in range(st_col, en_col + 1):
            if r != row or c != col:
                my_neighbors.append((r, c))
    return my_neighbors


def live(board: Matrix, cells: Vector) -> Vector:
    live_cells: Vector = []
    for row, col in cells:
        if board[row][col] > 0:
            live_cells.append((row, col))
    return live_cells


def game_of_life(board_size: int, steps: int, initial_state: Vector):
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    for row, col in initial_state:
        board[row][col] = 1
    print_board(board, 0, True)
    for t in range(1, steps + 1):
        marked_for_life: Vector = []
        marked_for_death: Vector = []
        for row in range(board_size):
            for col in range(board_size):
                # A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
                my_neighbors = neighbors(board_size, (row, col))
                neighbors_alive = live(board, my_neighbors)
                if board[row][col] > 0:
                    # Any live cell with less than two live neighbours dies.
                    # Any live cell with more than three live neighbours dies.
                    if len(neighbors_alive) < 2 or len(neighbors_alive) > 3:
                        marked_for_death.append((row, col))
                    # Any live cell with two or three live neighbours remains living.
                else:
                    # Any dead cell with exactly three live neighbours becomes a live cell.
                    if len(neighbors_alive) == 3:
                        marked_for_life.append((row, col))
        # print(f"{t}: {marked_for_life} - {marked_for_death}")
        for row in range(board_size):
            for col in range(board_size):
                if (row, col) in marked_for_death:
                    board[row][col] = 0
                if (row, col) in marked_for_life:
                    board[row][col] = 1
        print_board(board, t, True)


if __name__ == "__main__":
    game_of_life(3, 10, [(0, 0), (1, 1), (2, 2)])
    game_of_life(5, 10, [(0, 1), (1, 2), (1, 1), (1, 3), (2, 3), (2, 2)])
