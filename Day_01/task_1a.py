import re


def find_calibration_values(filename):
    calibration_values = []
    with open(filename, "r") as f:
        for line in f.readlines():
            first = re.findall(r"\d", line)[0]
            last = re.findall(r"\d", line)[-1]
            calibration_values.append(int(first + last))
    return calibration_values


if "__main__" == __name__:
    print(sum(find_calibration_values("Day_01/puzzle_input.txt")))
