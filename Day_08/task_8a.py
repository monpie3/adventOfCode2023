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


def count_steps(filename):
    with open(filename) as f:
        instructions, _, *nodes = f.read().splitlines()
    nodes = parse_nodes(nodes)

    current_node = "AAA"
    max_ind = len(instructions) - 1
    ind = 0
    steps = 0

    while current_node != "ZZZ":
        if instructions[ind] == "R":
            current_node = go_right(current_node, nodes)
        elif instructions[ind] == "L":
            current_node = go_left(current_node, nodes)
        ind = ind + 1 if ind < max_ind else 0
        # ind += 1 if ind < max_ind else 0
        # diffrent result because here addition is conditional
        steps += 1

    return steps


if "__main__" == __name__:
    print(count_steps("Day_08/puzzle_input.txt"))
