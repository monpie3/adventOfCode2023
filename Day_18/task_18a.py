from enum import Enum
import itertools


class Direction(Enum):
    R = (0, 1)
    L = (0, -1)
    U = (-1, 0)
    D = (1, 0)


def move_to_next_edge(current_pos, direction, step_num):
    x, y = current_pos
    dx, dy = Direction[direction].value
    return (x + dx * step_num, y + dy * step_num)


def lagoon_capacity(filename) -> float:
    current_pos = (0, 0)
    edges = [current_pos]
    perimeter = 0

    with open(filename) as f:
        for line in f:
            direction, step_num, _ = line.split()
            perimeter += int(step_num)
            current_pos = move_to_next_edge(current_pos, direction, int(step_num))
            edges.append(current_pos)

    # shoelace formula to get the polygon area
    area = shoelace(edges)
    # pick's theorem to get the num of fields  A = I + B/2 - 1  -> I + B = A + B/2 + 1
    return area + perimeter / 2 + 1


def shoelace(edges) -> float:
    """
    Calculate the area of the polygon using the shoelace formula
    """
    area = 0
    for (x0, y0), (x1, y1) in itertools.pairwise(edges):
        area += x0 * y1 - y0 * x1
    return abs(area / 2.0)


if __name__ == "__main__":
    print(lagoon_capacity("Day_18/puzzle_input.txt"))
