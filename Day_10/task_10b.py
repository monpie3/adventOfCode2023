import copy
import itertools

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

    up_and_down = [
        (start_row + dr, start_col)
        for dr in [-1, 1]
        if 0 <= start_row + dr < map_height
    ]

    left_and_right = [
        (start_row, start_col + dc) for dc in [-1, 1] if 0 <= start_col + dc < map_width
    ]

    points_to_explore = up_and_down + left_and_right

    return points_to_explore


def explore_direction(current_row, current_col, start_row, start_col, sketch):
    previous_row, previous_col = start_row, start_col

    # important line - without it, the sketch can be modified during the exploration
    sketch = copy.deepcopy(sketch)
    tiles = [(start_row, start_col), (current_row, current_col)]

    while (current_row, current_col) not in [(start_row, start_col), (-1, -1)]:
        next_row, next_col = go_to_next_tile(
            previous_row, previous_col, current_row, current_col, sketch
        )

        tiles.append((next_row, next_col))

        # what was previously current, now is previous
        previous_row, previous_col = current_row, current_col

        # what was previously next, now is current
        current_row, current_col = next_row, next_col

    if type(sketch[previous_row][previous_col]) != int:
        return 0
    return tiles


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


def shoelace(edges) -> float:
    """
    Calculate the area of the polygon using the shoelace formula
    """
    area = 0
    for (x0, y0), (x1, y1) in itertools.pairwise(edges):
        area += x0 * y1 - y0 * x1
    return abs(area / 2.0)


def count_enclosed_tiles(filename):
    with open(filename) as f:
        map_str = f.read().split()

    sketch = [list(row) for row in map_str]

    # find the starting point
    start_row, start_col = find_starting_tile(sketch)
    sketch[start_row][start_col] = 1

    # scan pipes near the starting point
    points_to_explore = find_tiles_nearby(sketch, start_row, start_col)

    paths = []
    for current_point in points_to_explore:
        current_row, current_col = current_point
        tiles = explore_direction(
            current_row, current_col, start_row, start_col, sketch
        )
        if tiles != 0:
            paths.append(tiles)

    # leave only path with the biggest number of tiles
    max_length = max(len(path) for path in paths)
    paths = [path for path in paths if len(path) == max_length]

    # ignore duplicates
    path = paths[0]

    # shoelace formula to get the polygon area
    area = shoelace(path)

    # pick's theorem to get the num of fields inside
    # A = I + B/2 - 1
    # I - number of interior points
    # B - number of boundary points
    # A - area of the polygon
    # I = A - B/2 + 1
    num_of_boundary_points = len(path) - 1
    num_interior_points = int(abs(area) - 0.5 * num_of_boundary_points + 1)

    return num_interior_points


if "__main__" == __name__:
    print(count_enclosed_tiles("Day_10/puzzle_input.txt"))
