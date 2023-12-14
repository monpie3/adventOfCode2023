import pandas as pd


def process_input(file_content):
    image = [list(line) for line in file_content.split()]
    return pd.DataFrame(
        image, index=range(1, len(image) + 1), columns=range(1, len(image[0]) + 1)
    )


def find_index(diffrence, left_pattern_ind, all_duplicates_ind, pattern_map):
    item = 1
    possible_indices = [i for i in range(len(diffrence)) if diffrence[i] == item]

    for possible_id in possible_indices:
        possible_line = left_pattern_ind[possible_id]

        distance_from_line_to_end = len(pattern_map) - possible_line - 1
        # -1 because possible_line is duplicated
        distance_from_start_to_line = possible_line - 1
        # -1 - don't count possible_line
        how_many_times_repeat = min(
            distance_from_line_to_end, distance_from_start_to_line
        )

        # check if you have enough duplicates in all_duplicates
        is_it_possible = True

        for left_values in range(possible_line - how_many_times_repeat, possible_line):
            if left_values not in all_duplicates_ind:
                is_it_possible = False

        for right_values in range(
            possible_line + 2, possible_line + 2 + how_many_times_repeat
        ):
            if right_values not in all_duplicates_ind:
                is_it_possible = False

        if is_it_possible:
            return possible_id
    return -1


def check_reflection(pattern_map):
    left_pattern = pattern_map[pattern_map.duplicated(keep="last")]
    sorted_left_pattern = left_pattern.sort_values(
        by=list(left_pattern.columns), axis=0
    )
    left_pattern_ind = sorted_left_pattern.index.values

    right_pattern = pattern_map[pattern_map.duplicated(keep="first")]
    sorted_right_pattern = right_pattern.sort_values(
        by=list(right_pattern.columns), axis=0
    )
    right_pattern_ind = sorted_right_pattern.index.values

    diffrence = right_pattern_ind - left_pattern_ind

    if 1 not in diffrence:
        # No possible reflection line found
        return []

    all_duplicates_ind = pattern_map[pattern_map.duplicated(keep=False)].index.values

    if 1 not in all_duplicates_ind and len(pattern_map) not in all_duplicates_ind:
        # There is no possibility this is a reflection line
        return []

    ind = find_index(diffrence, left_pattern_ind, all_duplicates_ind, pattern_map)
    if ind == -1:
        return []
    reflection_line = left_pattern_ind[ind]
    return reflection_line


def find_reflection_line(pattern_map):
    pattern_map = process_input(pattern_map)
    # Find duplicate rows
    vertical_line = check_reflection(pattern_map)
    if vertical_line:
        return vertical_line * 100
    # Find duplicate columns
    transformed_pattern_map = pattern_map.T
    horizontal_reflection = check_reflection(transformed_pattern_map)
    if horizontal_reflection:
        return horizontal_reflection
    raise Exception("No reflection found")


def summarize_pattern_notes(filename):
    summary = []
    with open(filename) as f:
        pattern_maps = f.read().split("\n\n")

    for pattern_map in pattern_maps:
        summary.append(find_reflection_line(pattern_map))
    return sum(summary)


if "__main__" == __name__:
    print(summarize_pattern_notes("Day_13/puzzle_input.txt"))
