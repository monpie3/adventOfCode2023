def go_down(current_line):
    sequence_below = []
    if len(set(current_line)) == 1:
        # all elements have the same value
        return [0] * (len(current_line) - 1)

    for ind in range(len(current_line) - 1):
        sequence_below.append(current_line[ind + 1] - current_line[ind])
    return sequence_below


def go_up(sequences):
    for ind in range(len(sequences) - 1, 0, -1):
        last_el_last_line = sequences[ind][-1]
        last_el_line_above = sequences[ind - 1][-1]
        sequences[ind - 1].append(last_el_last_line + last_el_line_above)
    return sequences[0][-1]


def extrapolate_history(line):
    current_line = list(map(int, line.split()))
    is_all_zero = False
    sequences = [current_line]

    # go down
    while not is_all_zero:
        line_below = go_down(current_line)
        sequences.append(line_below)
        is_all_zero = all([x == 0 for x in line_below])
        current_line = line_below

    # go up
    return go_up(sequences)


if "__main__" == __name__:
    history = []
    with open("Day_09/puzzle_input.txt") as file:
        for line in file:
            history.append(extrapolate_history(line))

    print(sum(history))
