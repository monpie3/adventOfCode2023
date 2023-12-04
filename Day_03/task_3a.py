import re
import string

# remove the dot from the punctuation values
SYMBOLS = string.punctuation.replace(".", "")


def is_number_adjacent_to_symbol(num, row_ind, schematic):
    # remove the \n from the end of the line
    line_to_consider = schematic[row_ind].strip()
    last_available_index = len(line_to_consider) - 1

    column_start = num.start()
    column_end = num.end() - 1

    # possible locaton of the symbol
    if column_start > 0:
        column_start = column_start - 1

    if last_available_index > column_end:
        column_end = column_end + 1

    # check if the number adjacent to a symbol
    # <- from the number
    if line_to_consider[column_start] in SYMBOLS:
        return True
    # -> from the number
    if line_to_consider[column_end] in SYMBOLS:
        return True

    # ↑ the number
    if row_ind > 0:
        line_above = schematic[row_ind - 1]
        line_to_check = line_above[column_start : column_end + 1]
        if any([char_to_check in SYMBOLS for char_to_check in line_to_check]):
            return True

    # ↓ the number
    if row_ind < len(schematic) - 1:
        line_below = schematic[row_ind + 1]
        line_to_check = line_below[column_start : column_end + 1]
        if any([char_to_check in SYMBOLS for char_to_check in line_to_check]):
            return True
    return False


def evaluate_engine_schematic(schematic):
    part_number = []
    for row_ind in range(len(schematic)):
        # find numbers
        numbers_location = re.finditer(r"\d+", schematic[row_ind])

        for num in numbers_location:
            if is_number_adjacent_to_symbol(num, row_ind, schematic):
                part_number.append(int(num.group()))
    return part_number


def find_part_numbers(filename):
    with open(filename, "r") as file:
        schematic = file.readlines()

    part_number = evaluate_engine_schematic(schematic)
    return part_number


if __name__ == "__main__":
    print(sum(find_part_numbers("Day_03/puzzle_input.txt")))
