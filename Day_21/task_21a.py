from typing import Tuple


def process_input(filename):
    with open(filename) as f:
        tiles = f.read().splitlines()

    for row, line in enumerate(tiles):
        if "S" in line:
            col = line.index("S")
            start = (row, col)  # save start position

    tiles = [list(line) for line in tiles]
    tiles[row][col] = "."  # replace start position with garden plot
    return tiles, start


def print_tiles(tiles, possible_moves) -> None:
    """Side efect: changes tiles list"""
    for move in possible_moves:
        tiles[move[0]][move[1]] = "O"

    for el in tiles:
        print("".join(el))


def get_possible_moves(current_point, tiles, max_width, max_height) -> Tuple[int, int]:
    row, col = current_point
    possible_moves = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)

    # filter out of bounds
    possible_moves = [move for move in possible_moves if move[0] >= 0 and move[1] >= 0]
    possible_moves = [
        move for move in possible_moves if move[0] < max_height and move[1] < max_width
    ]

    # filter rocks
    possible_moves = filter(lambda move: tiles[move[0]][move[1]] != "#", possible_moves)

    return list(set(possible_moves))


def count_garden_plots(filename: str, step_limit: int) -> int:
    tiles, start = process_input(filename)

    max_width = len(tiles[0])
    max_height = len(tiles)

    stack = [start]
    step = 0

    while stack and step < step_limit:
        step += 1
        possible_moves_per_step = set()
        while stack:
            current_tile = stack.pop()
            current_moves = get_possible_moves(
                current_tile, tiles, max_width, max_height
            )
            possible_moves_per_step.update(current_moves)
        stack.extend(possible_moves_per_step)

    print("possible_moves", possible_moves_per_step)
    return len(possible_moves_per_step)


if "__main__" == __name__:
    print(count_garden_plots("Day_21/puzzle_input.txt", step_limit=64))
