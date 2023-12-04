import math
import re


def find_gear_ratio(filename):
    gears = {}
    symbol = "*"

    with open(filename, "r") as file:
        lines = file.readlines()

    # go through all the lines
    for row_ind in range(len(lines)):
        # remove the \n from the end of the line
        line_to_consider = lines[row_ind].strip()
        last_available_index = len(line_to_consider) - 1

        # find the numbers
        numbers_location = re.finditer(r"\d+", line_to_consider)

        for num in numbers_location:
            is_num_adjacent_to_symbol = False

            column_start = num.start()
            column_end = num.end() - 1
            num = int(num.group())

            # possible locaton of the symbol
            if column_start > 0:
                column_start = column_start - 1

            if last_available_index > column_end:
                column_end = column_end + 1

            # check if the number adjacent to a symbol
            # <-- from the number
            if line_to_consider[column_start] in symbol:
                is_num_adjacent_to_symbol = True
                symbol_row = row_ind
                symbol_column = column_start
            # --> from the number
            elif line_to_consider[column_end] in symbol:
                is_num_adjacent_to_symbol = True
                symbol_row = row_ind
                symbol_column = column_end
            # ↑ the number
            else:
                if row_ind > 0:
                    line_above = lines[row_ind - 1]
                    line_to_check = line_above[column_start : column_end + 1]
                    stars_location = re.finditer(r"\*", line_to_check)
                    for star in stars_location:
                        symbol_row = row_ind - 1
                        symbol_column = column_start + star.start()
                        if (symbol_row, symbol_column) in gears.keys():
                            gears[(symbol_row, symbol_column)].append(num)
                        else:
                            gears[(symbol_row, symbol_column)] = [num]

                # ↓ the number
                if row_ind < len(lines) - 1:
                    line_below = lines[row_ind + 1]
                    line_to_check = line_below[column_start : column_end + 1]
                    stars_location = re.finditer(r"\*", line_to_check)
                    for star in stars_location:
                        symbol_row = row_ind + 1
                        symbol_column = column_start + star.start()
                        if (symbol_row, symbol_column) in gears.keys():
                            gears[(symbol_row, symbol_column)].append(num)
                        else:
                            gears[(symbol_row, symbol_column)] = [num]

            if is_num_adjacent_to_symbol:
                if (symbol_row, symbol_column) in gears.keys():
                    gears[(symbol_row, symbol_column)].append(num)
                else:
                    gears[(symbol_row, symbol_column)] = [num]

    return gears


if __name__ == "__main__":
    gears = find_gear_ratio("Day_03/puzzle_input.txt")
    gear_ratio = []
    for key in gears.keys():
        if len(gears[key]) > 1:
            gear_ratio.append(math.prod(gears[key]))

    print(sum(gear_ratio))
