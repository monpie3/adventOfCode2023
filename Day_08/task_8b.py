import math


def go_right(node, nodes):
    return nodes[node][1]


def go_left(node, nodes):
    return nodes[node][0]


def parse_nodes(nodes):
    output = {}
    for m_node in nodes:
        destinaton, instructions = m_node.split(" = ")
        a, b = instructions[1:9].split(", ")
        output[destinaton] = (a, b)
    return output


def steps_to_first_Z(start_node, nodes, instructions):
    current_node = start_node
    steps = 0
    ind = 0
    max_ind = len(instructions) - 1
    while not current_node.endswith("Z"):
        if instructions[ind] == "R":
            current_node = go_right(current_node, nodes)

        elif instructions[ind] == "L":
            current_node = go_left(current_node, nodes)

        ind = ind + 1 if ind < max_ind else 0
        steps += 1
    return steps


def count_min_steps(filename):
    with open(filename) as f:
        instructions, _, *nodes = f.read().splitlines()
    nodes = parse_nodes(nodes)

    start_nodes = [node for node in nodes.keys() if node.endswith("A")]

    steps_list = []
    for start_node in start_nodes:
        steps_list.append(steps_to_first_Z(start_node, nodes, instructions))

    # because puzzle input is constructed in such a way
    # that the node sequences from A to Z are periodic we can use LCM
    return math.lcm(*steps_list)


if "__main__" == __name__:
    print(count_min_steps("Day_08/puzzle_input.txt"))
