def process_input(filename):
    with open(filename) as f:
        initialization_sequence = f.read().split(",")
    initialization_sequence = [el.strip() for el in initialization_sequence]
    return initialization_sequence


def hash_algorithm(string):
    current_value = 0
    for el in string:
        current_value += ord(el)
        current_value = current_value * 17 % 256
    return current_value


def sum_of_hash(filename):
    initialization_sequence = process_input(filename)
    hash = 0
    for sequence in initialization_sequence:
        hash += hash_algorithm(sequence)
    return hash


if __name__ == "__main__":
    print(sum_of_hash("Day_15/puzzle_input.txt"))
