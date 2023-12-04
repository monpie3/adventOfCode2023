import re
import string


def check_if_line_contains_symbol(line_to_check, column_start, column_end, symbols):
    line_to_check = line_to_check[column_start : column_end + 1]
    return any([char_to_check in symbols for char_to_check in line_to_check])


def find_part_numbers(filename):
    part_number = []
    # remove . from the punctuation values
    symbols = string.punctuation.replace(".", "")

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
            num = num.group()

            # possible locaton of the symbol
            if column_start > 0:
                column_start = column_start - 1

            if last_available_index > column_end:
                column_end = column_end + 1

            # check if the number adjacent to a symbol
            # <-- from the number
            if line_to_consider[column_start] in symbols:
                is_num_adjacent_to_symbol = True
            # --> from the number
            elif line_to_consider[column_end] in symbols:
                is_num_adjacent_to_symbol = True
            # ↑ the number
            else:
                if row_ind > 0:
                    line_above = lines[row_ind - 1]
                    if check_if_line_contains_symbol(
                        line_above, column_start, column_end, symbols
                    ):
                        is_num_adjacent_to_symbol = True

                # ↓ the number
                if row_ind < len(lines) - 1:
                    line_below = lines[row_ind + 1]
                    if check_if_line_contains_symbol(
                        line_below, column_start, column_end, symbols
                    ):
                        is_num_adjacent_to_symbol = True

            if is_num_adjacent_to_symbol:
                part_number.append(int(num))
    return part_number


if __name__ == "__main__":
    print(sum(find_part_numbers("Day_03/puzzle_input.txt")))
