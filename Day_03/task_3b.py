import math
import re


SYMBOL = "*"


def get_star_location(num, row_ind, schematic):
    location = []
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
    if line_to_consider[column_start] == SYMBOL:
        location.append((row_ind, column_start))
    # -> from the number
    if line_to_consider[column_end] == SYMBOL:
        location.append((row_ind, column_end))
    # ↑ the number
    if row_ind > 0 and SYMBOL in schematic[row_ind - 1][column_start : column_end + 1]:
        stars_location = re.finditer(
            r"\*", schematic[row_ind - 1][column_start : column_end + 1]
        )
        for star in stars_location:
            symbol_row = row_ind - 1
            symbol_column = column_start + star.start()
            location.append((symbol_row, symbol_column))

    # ↓ the number
    if (
        row_ind < len(schematic) - 1
        and SYMBOL in schematic[row_ind + 1][column_start : column_end + 1]
    ):
        stars_location = re.finditer(
            r"\*", schematic[row_ind + 1][column_start : column_end + 1]
        )
        for star in stars_location:
            symbol_row = row_ind + 1
            symbol_column = column_start + star.start()
            location.append((symbol_row, symbol_column))
    return location


def organize_gears(star_location, gears, num):
    if star_location in gears.keys():
        gears[star_location].append(num)
    else:
        gears[star_location] = [num]


def find_gear_ratio(filename):
    gears = {}

    with open(filename, "r") as file:
        schematic = file.readlines()

    # go through all the lines
    for row_ind in range(len(schematic)):
        # find numbers
        numbers_location = re.finditer(r"\d+", schematic[row_ind])

        for num in numbers_location:
            star_location = get_star_location(num, row_ind, schematic)
            num = int(num.group())

            if len(star_location) == 1:
                organize_gears(star_location[0], gears, num)
            elif len(star_location) > 1:
                for location in star_location:
                    organize_gears(location, gears, num)
    return gears


if __name__ == "__main__":
    gears = find_gear_ratio("Day_03/puzzle_input.txt")
    gear_ratio = []
    for key in gears.keys():
        if len(gears[key]) > 1:
            gear_ratio.append(math.prod(gears[key]))

    print(sum(gear_ratio))
