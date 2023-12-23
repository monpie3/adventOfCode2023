from typing import Tuple, List


def process_input(filename):
    with open(filename) as f:
        tiles = f.read().splitlines()

    tiles = [list(line) for line in tiles]
    return tiles


def get_possible_moves(
    current_point, visited, tiles, max_width, max_height
) -> Tuple[int, int]:
    row, col = current_point
    if tiles[row][col] == ".":
        possible_moves = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
    # steep slopes
    elif tiles[row][col] == "^":
        possible_moves = ((row - 1, col),)
    elif tiles[row][col] == "v":
        possible_moves = ((row + 1, col),)
    elif tiles[row][col] == ">":
        possible_moves = ((row, col + 1),)
    elif tiles[row][col] == "<":
        possible_moves = ((row, col - 1),)
    else:
        raise Exception("Unknown tile")

    # filter out of bounds
    possible_moves = [move for move in possible_moves if move[0] >= 0 and move[1] >= 0]
    possible_moves = [
        move for move in possible_moves if move[0] < max_height and move[1] < max_width
    ]

    # filter visited
    possible_moves = [move for move in possible_moves if move not in visited]

    # filter forest
    possible_moves = filter(lambda move: tiles[move[0]][move[1]] != "#", possible_moves)

    return set(possible_moves)


def count_steps_to_meta(filename: str) -> List[int]:
    tiles = process_input(filename)
    max_width = len(tiles[0])
    max_height = len(tiles)

    start_col = tiles[0].index(".")
    start = (0, start_col)
    end_col = tiles[-1].index(".")
    end = (max_height - 1, end_col)

    steps_to_meta = []
    step = 0
    visited = set()
    visited.add(start)
    stack = [(start, step, visited)]

    while stack:
        current_tile, step, visited = stack.pop()
        step += 1

        possible_moves = get_possible_moves(
            current_tile, visited, tiles, max_width, max_height
        )

        for move in possible_moves:
            if move == end:
                steps_to_meta.append(step)
                continue

            if len(possible_moves) > 1:
                visited = visited.copy()

            visited.add(move)
            stack.append((move, step, visited))

    print("steps_to_meta", steps_to_meta)
    return steps_to_meta


if "__main__" == __name__:
    print(max(count_steps_to_meta("Day_23/puzzle_input.txt")))
