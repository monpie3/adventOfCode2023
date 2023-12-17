from enum import Enum
from typing import List, Tuple, Set


class Fields(Enum):
    EMPTY_SPACE = "."
    MIRROR_SLASH = "/"
    MIRROR_BACKSLASH = "\\"
    SPLITTER_VERTICAL = "|"
    SPLITTER_HORIZONTAL = "-"


def parse_input(filename: str) -> List:
    with open(filename) as f:
        f = f.read().splitlines()
    return [list(line.strip()) for line in f]


def change_direction_by_mirror(current_el: str, direction: str) -> str:
    if (current_el == Fields.MIRROR_SLASH.value and direction == ">") or (
        current_el == Fields.MIRROR_BACKSLASH.value and direction == "<"
    ):
        direction = "^"

    elif (current_el == Fields.MIRROR_SLASH.value and direction == "<") or (
        current_el == Fields.MIRROR_BACKSLASH.value and direction == ">"
    ):
        direction = "V"

    elif (current_el == Fields.MIRROR_SLASH.value and direction == "^") or (
        current_el == Fields.MIRROR_BACKSLASH.value and direction == "V"
    ):
        direction = ">"

    elif (current_el == Fields.MIRROR_SLASH.value and direction == "V") or (
        current_el == Fields.MIRROR_BACKSLASH.value and direction == "^"
    ):
        direction = "<"
    return direction


def move(
    current_position: Tuple[int, int],
    direction: str,
    contraption: List,
    energized_tiles,
) -> Tuple[int, int]:
    if current_position == (-1, -1):
        return energized_tiles

    width = len(contraption[0])
    height = len(contraption)

    row, col = current_position
    current_el = contraption[row][col]

    if (
        current_el == Fields.MIRROR_SLASH.value
        or current_el == Fields.MIRROR_BACKSLASH.value
    ):
        direction = change_direction_by_mirror(current_el, direction)

    if current_el == Fields.SPLITTER_HORIZONTAL.value and direction in ["^", "V"]:
        energized_tiles = move(current_position, ">", contraption, energized_tiles)
        energized_tiles = move(current_position, "<", contraption, energized_tiles)
        return energized_tiles

    elif current_el == Fields.SPLITTER_VERTICAL.value and direction in [">", "<"]:
        energized_tiles = move(current_position, "^", contraption, energized_tiles)
        energized_tiles = move(current_position, "V", contraption, energized_tiles)
        return energized_tiles

    else:
        if current_el == Fields.EMPTY_SPACE.value or current_el in ["^", "V", "<", ">"]:
            if contraption[row][col] == direction:
                # loop
                return energized_tiles
            else:
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
            # otherwise - out of range
            next_position = (row, col)
            energized_tiles.append(next_position)
            move(next_position, direction, contraption, energized_tiles)

    return energized_tiles


def enter_beam(contraption: List):
    current_position = (0, 0)
    energized_tiles = [current_position]
    energized_tiles = move(current_position, ">", contraption, energized_tiles)
    return energized_tiles


def get_num_of_energized_titles(filename: str):
    contraption = parse_input(filename)
    energized_tiles = enter_beam(contraption)

    return len(set(energized_tiles))


if __name__ == "__main__":
    print(get_num_of_energized_titles("Day_16/puzzle_input.txt"))
