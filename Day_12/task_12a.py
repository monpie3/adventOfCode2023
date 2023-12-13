import re
import itertools


def get_coordinates_of_unknown_springs(springs):
    return [ind for ind, el in enumerate(springs) if el == "?"]


def parse_record(record):
    return list(map(int, record.split(",")))


def check_if_possible(springs, record):
    chunks = re.findall(r"#+", springs)
    for ind, el in enumerate(record):
        if len(chunks[ind]) != el:
            return False
    return True


def replace_unknown_with_spring(springs, ids_to_replace):
    for unknown_id in ids_to_replace:
        springs = list(springs)
        springs[unknown_id] = "#"
    return "".join(springs)


def get_num_of_possible_arrangements(springs, record):
    record = parse_record(record)
    to_find = sum(record) - springs.count("#")
    coordinates = get_coordinates_of_unknown_springs(springs)
    ids_to_replace = itertools.combinations(coordinates, r=to_find)

    num_of_possible_arrangements = 0
    for id_to_replace in list(ids_to_replace):
        new_string = replace_unknown_with_spring(springs, id_to_replace)

        if check_if_possible(new_string, record):
            num_of_possible_arrangements += 1

    return num_of_possible_arrangements


if "__main__" == __name__:
    num_of_possible_arrangements = 0
    with open("Day_12/puzzle_input.txt") as f:
        possible_arrangements = []
        for line in f:
            springs, record = line.split(" ")
            num_of_possible_arrangements += get_num_of_possible_arrangements(
                springs, record
            )
    print(num_of_possible_arrangements)
