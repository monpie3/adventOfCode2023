import copy
from typing import List, Tuple, Set


def parse_input(filename: str) -> List:
    with open(filename) as f:
        f = f.read().splitlines()
    return [list(line.strip()) for line in f]


def change_direction_by_mirror(current_el: str, direction: str) -> str:
    if (current_el == "/" and direction == ">") or (
        current_el == "\\" and direction == "<"
    ):
        direction = "^"

    elif (current_el == "/" and direction == "<") or (
        current_el == "\\" and direction == ">"
    ):
        direction = "V"

    elif (current_el == "/" and direction == "^") or (
        current_el == "\\" and direction == "V"
    ):
        direction = ">"

    elif (current_el == "/" and direction == "V") or (
        current_el == "\\" and direction == "^"
    ):
        direction = "<"
    return direction


def move(
    current_position: Tuple[int, int],
    direction: str,
    contraption: List,
) -> Set[Tuple[int, int]]:
    width = len(contraption[0])
    height = len(contraption)

    energized_tiles = {current_position}
    stack = [(current_position, direction)]

    while stack:
        current_position, direction = stack.pop()

        row, col = current_position
        current_el = contraption[row][col]

        if current_el == "/" or current_el == "\\":
            direction = change_direction_by_mirror(current_el, direction)

        if current_el == "-" and direction in ["^", "V"]:
            stack.append((current_position, ">"))
            stack.append((current_position, "<"))

        elif current_el == "|" and direction in [">", "<"]:
            stack.append((current_position, "^"))
            stack.append((current_position, "V"))

        else:
            if current_el == "." or current_el in [
                "^",
                "V",
                "<",
                ">",
            ]:
                if contraption[row][col] == direction:
                    continue  # loop, we are going in the same direction
                contraption[row][col] = direction

            if direction == "^":
                row -= 1
            elif direction == "V":
                row += 1
            elif direction == "<":
                col -= 1
            elif direction == ">":
                col += 1

            if 0 <= row < height and 0 <= col < width:
                next_position = (row, col)
                energized_tiles.add(next_position)
                stack.append((next_position, direction))
    return len(energized_tiles)


def enter_beam(enter_position, enter_direction, contraption: List):
    contraption = copy.deepcopy(contraption)
    energized_tiles = move(enter_position, enter_direction, contraption)
    return energized_tiles


def get_num_of_energized_titles(filename: str):
    contraption = parse_input(filename)
    width = len(contraption[0])
    height = len(contraption)

    energized_tiles_num = set()

    for col_ind in range(width):
        # top row
        energized_tiles_num.add(enter_beam((0, col_ind), "V", contraption))

        # bottom row
        energized_tiles_num.add(enter_beam((width - 1, col_ind), "^", contraption))

    for row_ind in range(width):
        # leftmost column
        energized_tiles_num.add(enter_beam((row_ind, 0), ">", contraption))

        # rightmost column
        energized_tiles_num.add(enter_beam((row_ind, height - 1), "<", contraption))

    return energized_tiles_num


if __name__ == "__main__":
    print(max(get_num_of_energized_titles("Day_16/puzzle_input.txt")))
