from collections import defaultdict


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


def find_lens_id(box_content, label):
    for box_el in box_content:
        el_label, _ = box_el
        if el_label == label:
            return box_content.index(box_el)
    return -1


def prepare_boxes(initialization_sequence):
    boxes_container = defaultdict(list)

    for sequence in initialization_sequence:
        if "=" in sequence:
            label, focal_length = sequence.split("=")
        else:
            label, _ = sequence.split("-")

        box_num = hash_algorithm(label)

        box_content = boxes_container[box_num]
        lens_id = find_lens_id(box_content, label)

        if "=" in sequence:
            if lens_id != -1:
                # replace the lens with the given label
                # if it is present in the box
                box_content[lens_id] = (label, focal_length)
            else:
                # add the lens with the given label
                boxes_container[box_num].append((label, focal_length))
        else:
            # remove the lens with the given label
            # if it is present in the box
            if lens_id != -1:
                box_content.pop(lens_id)
    return boxes_container


def get_focusing_power(filename):
    initialization_sequence = process_input(filename)
    boxes = prepare_boxes(initialization_sequence)
    focusing_power = 0
    for box_num, lenses in boxes.items():
        for ind, lens in enumerate(lenses):
            _, focal_length = lens
            slot_num = ind + 1
            focusing_power += (box_num + 1) * slot_num * int(focal_length)
    return focusing_power


if __name__ == "__main__":
    print(get_focusing_power("Day_15/puzzle_input.txt"))
