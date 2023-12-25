import itertools
import collections


def parse_input(filename):
    hailstone = collections.namedtuple("hailstone", ["x", "y", "dx", "dy"])
    container = []

    with open(filename) as f:
        for line in f:
            position, velocity = line.strip().split(" @ ")
            px, py, _ = position.split(",")
            vx, vy, _ = velocity.split(",")
            container.append(hailstone(int(px), int(py), int(vx), int(vy)))
    return container


def count_intersection(filename, min_window, max_window):
    container = parse_input(filename)
    collision = 0

    to_check = list(itertools.combinations(container, 2))
    for hailstone_a, hailstone_b in to_check:
        a_a = hailstone_a.dy / hailstone_a.dx
        a_b = hailstone_b.dy / hailstone_b.dx

        b_a = hailstone_a.y - a_a * hailstone_a.x
        b_b = hailstone_b.y - a_b * hailstone_b.x

        if a_a == a_b:
            # parallel
            continue

        x_cross = (b_b - b_a) / (a_a - a_b)
        y_cross = a_a * x_cross + b_a

        # verify not in the past
        if (
            (x_cross < hailstone_a.x and hailstone_a.dx > 0)
            or (x_cross > hailstone_a.x and hailstone_a.dx < 0)
            or (x_cross < hailstone_b.x and hailstone_b.dx > 0)
            or (x_cross > hailstone_b.x and hailstone_b.dx < 0)
        ):
            continue

        # verify if in the window
        if min_window <= x_cross <= max_window and min_window <= y_cross <= max_window:
            collision += 1
    return collision


if "__main__" == __name__:
    min_window = 200000000000000
    max_window = 400000000000000

    print(count_intersection("Day_24/puzzle_input.txt", min_window, max_window))
