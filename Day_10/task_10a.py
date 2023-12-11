import copy


RULES = {
    "-": [[0, 1], [0, -1]],  # - is a horizontal pipe connecting east and west
    "|": [[-1, 0], [1, 0]],  # | is a vertical pipe connecting north and south
    "L": [[-1, 0], [0, 1]],  # L is a 90-degree bend connecting north and east
    "J": [[-1, 0], [0, -1]],  # J is a 90-degree bend connecting north and west
    "7": [[1, 0], [0, -1]],  # 7 is a 90-degree bend connecting south and west
    "F": [[1, 0], [0, 1]],  # F is a 90-degree bend connecting south and east
}


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def find_starting_tile(sketch):
    return index_2d(sketch, "S")


def find_tiles_nearby(sketch, start_row, start_col):
    map_width = len(sketch[0])
    map_height = len(sketch)
    points_to_explore = []

    if start_row - 1 >= 0:
        up_tile = start_row - 1, start_col
        points_to_explore.append(up_tile)
    if start_row + 1 < map_height:
        down_tile = start_row + 1, start_col
        points_to_explore.append(down_tile)
    if start_col - 1 >= 0:
        left_tile = start_row, start_col - 1
        points_to_explore.append(left_tile)
    if start_col + 1 < map_width:
        right_tile = start_row, start_col + 1
        points_to_explore.append(right_tile)
    return points_to_explore


def explore_direction(current_row, current_col, start_row, start_col, sketch):
    previous_row, previous_col = start_row, start_col
    sketch = copy.deepcopy(
        sketch
    )  # important line - without it, the sketch can be modified during the exploration

    while (current_row, current_col) != (start_row, start_col) and (
        current_row,
        current_col,
    ) != (-1, -1):
        next_row, next_col = go_to_next_tile(
            previous_row, previous_col, current_row, current_col, sketch
        )
        previous_row, previous_col = (
            current_row,
            current_col,
        )  # what was previously current, now is previous
        current_row, current_col = (
            next_row,
            next_col,
        )  # what was previously next, now is current

    if type(sketch[previous_row][previous_col]) != int:
        return 0
    return sketch[previous_row][previous_col]


def go_to_next_tile(previous_row, previous_col, current_row, current_col, sketch):
    current_point = sketch[current_row][current_col]

    if current_point == ".":
        # we are in the dead end
        return -1, -1

    possible_moves = RULES[current_point]
    for move in possible_moves:
        move_row, move_col = move
        next_row, next_col = current_row + move_row, current_col + move_col
        if (next_row, next_col) != (previous_row, previous_col):
            if not type(current_point) == int:
                sketch[current_row][current_col] = (
                    sketch[previous_row][previous_col] + 1
                )
            return next_row, next_col

    # that means that we are in the dead end
    return -1, -1


def get_step_number(filename):
    with open(filename) as f:
        map_str = f.read().split()

    sketch = [list(row) for row in map_str]

    # find the starting point
    start_row, start_col = find_starting_tile(sketch)
    sketch[start_row][start_col] = 1

    # scan pipes near the starting point
    points_to_explore = find_tiles_nearby(sketch, start_row, start_col)

    steps = []
    for current_point in points_to_explore:
        current_row, current_col = current_point
        step_no = explore_direction(
            current_row, current_col, start_row, start_col, sketch
        )
        steps.append(step_no)

    print(steps)
    return max(steps) // 2


if "__main__" == __name__:
    print(get_step_number("Day_10/puzzle_input.txt"))
