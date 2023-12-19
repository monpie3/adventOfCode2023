from typing import Tuple


def parse_input(filename: str):
    workflows_dict = dict()

    with open(filename) as f:
        workflows, parts = f.read().split("\n\n")

    # parse workflows
    for workflow in workflows.splitlines():
        instr_start = workflow.find("{")
        workflow_name = workflow[:instr_start]
        instr = workflow[instr_start + 1 : -1].split(",")  # without curly braces
        workflows_dict[workflow_name] = instr

    # parse parts
    parts = parts.splitlines()
    parts_list = []
    for part in parts:
        part_dict = dict()
        part = part[1:-1].split(",")  # without curly braces
        for category in part:
            category_name, category_rate = category.split("=")
            part_dict[category_name] = int(category_rate)
        parts_list.append(part_dict)
    return workflows_dict, parts_list


def check_part(workflows: list, workflow_name, xmas: Tuple[int]) -> str:
    """Returns "A" if the part is accepted, "R" if the part is rejected."""
    x, m, a, s = xmas

    if workflow_name == "A" or workflow_name == "R":
        return workflow_name

    for ind, rule in enumerate(workflows[workflow_name]):
        if ind == len(workflows[workflow_name]) - 1:
            return check_part(workflows, rule, xmas)

        condition, result = rule.split(":")
        if eval(condition):
            return check_part(workflows, result, xmas)


def num_of_accepted_parts(filename):
    workflows, parts = parse_input(filename)

    accepted_parts = 0

    for part in parts:
        xmas = part["x"], part["m"], part["a"], part["s"]
        if check_part(workflows, "in", xmas) == "A":
            accepted_parts += sum(part.values())

    return accepted_parts


if __name__ == "__main__":
    print(num_of_accepted_parts("Day_19/puzzle_input.txt"))
