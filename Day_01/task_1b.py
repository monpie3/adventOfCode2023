import regex as re


spelled_out_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def extract_from_line(line):
    regex = r"\d|one|two|three|four|five|six|seven|eight|nine"
    result = re.findall(regex, line, overlapped=True)
    first_digit = result[0]
    last_digit = result[-1]
    if not first_digit.isnumeric():
        first_digit = spelled_out_numbers[first_digit]
    if not last_digit.isnumeric():
        last_digit = spelled_out_numbers[last_digit]
    return int(first_digit + last_digit)


def find_calibration_values(filename):
    calibration_values = []
    with open(filename, "r") as f:
        calibration_values = [extract_from_line(line) for line in f.readlines()]
    return calibration_values


if "__main__" == __name__:
    print(sum(find_calibration_values("Day_01/puzzle_input.txt")))
