def process_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def tilt_platfrom(str_col_line):
    if ".O" in str_col_line:
        return tilt_platfrom(str_col_line.replace(".O", "O."))
    # cant move if there is no ".O"
    return str_col_line


def calculate_load_on_beam(col_line):
    str_col_line = "".join(col_line)
    tilted = tilt_platfrom(str_col_line)
    rounded_rocks = [ind + 1 for ind, item in enumerate(tilted[::-1]) if item == "O"]
    return sum(rounded_rocks)


def get_total_load(filename):
    rocks_map = process_input(filename)
    t_rocks_map = list(map(list, zip(*rocks_map)))
    total_load = []
    for col_line in t_rocks_map:
        total_load.append(calculate_load_on_beam(col_line))
    return sum(total_load)


if "__main__" == __name__:
    print(get_total_load("Day_14/puzzle_input.txt"))
