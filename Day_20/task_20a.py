from typing import Tuple


def parse_modules(modules_configuration):
    output = {}
    conjunctions = []

    for current_module in modules_configuration:
        module_name, module_output = current_module.split(" -> ")
        module_type = module_name[0]
        if module_name == "broadcaster":
            module_type = "broadcaster"

        if module_type == "&":
            conjunctions.append(module_name[1:])

        if module_name != "broadcaster":
            module_name = module_name[1:]

        module_state = [module_type, tuple(module_output.split(", "))]

        if module_type == "%":
            module_state += ["off"]
        output[module_name] = module_state

    conjunction_dict = {}
    for conjunction in conjunctions:
        conjunction_temp = {}  # initialize dict for each conjunction with input modules
        for o_key, o_value in output.items():
            if conjunction in o_value[1]:
                conjunction_temp[o_key] = "low"
        conjunction_dict[conjunction] = conjunction_temp

    return output, conjunction_dict


def flip_flop_module(current_pulse, flip_flop_name, modules_configuration) -> str:
    """Flip-flop modules (prefix %) are either on or off; they are initially off.

    If a flip-flop module receives a high pulse, it is ignored and nothing happens.
    If a flip-flop module receives a low pulse, it flips between on and off.
        If it was off, it turns on and sends a high pulse.
        If it was on, it turns off and sends a low pulse.
    """
    if current_pulse == "high":
        # impulse is ignored
        return "ignore"

    if current_pulse == "low":
        flip_flop_state = modules_configuration[flip_flop_name][2]
        print("flip_flop_state", flip_flop_state)
        if flip_flop_state == "off":
            modules_configuration[flip_flop_name][2] = "on"
            return "high"
        if flip_flop_state == "on":
            modules_configuration[flip_flop_name][2] = "off"
            return "low"

    return "Unknown pulse"


def conjunction_module(conjunction_dict, conjuction_name) -> str:
    """Conjunction modules (prefix &) remember the type of the most recent pulse
    received from each of their connected input modules;

    they initially default to remembering a low pulse for each input.

    When a pulse is received:
    1) the conjunction module first updates its memory for that input.
    2) if there are high pulses for all inputs -> it sends a low pulse;
       otherwise, it sends a high pulse.
    """
    if set(conjunction_dict[conjuction_name].values()) == {"high"}:
        return "low"

    return "high"


def update_conjunction_dict(conjunction_dict, new_pulse, conjuction_name, input_module):
    conjunction_dict[conjuction_name][input_module] = new_pulse
    return conjunction_dict


def press_button(
    modules_configuration, conjunction_dict, conjunction_names
) -> Tuple[int, int]:
    print(f"button -low-> broadcaster")
    low = 1
    high = 0
    queue = [("broadcaster", "low")]

    while queue:
        current_module, current_pulse = queue.pop()

        if current_module not in modules_configuration:
            continue

        destination_modules = modules_configuration[current_module][1]
        current_module_type = modules_configuration[current_module][0]

        # when a module sends a pulse, it sends that type of pulse to each module
        # in its list of destination modules.
        if current_module_type == "%":  # flip_flop_module
            new_pulse = flip_flop_module(
                current_pulse, current_module, modules_configuration
            )
            if new_pulse == "ignore":
                continue
        elif current_module_type == "&":  # conjunction_module
            new_pulse = conjunction_module(conjunction_dict, current_module)
        else:
            new_pulse = current_pulse

        for destination_module in destination_modules:
            # counter update
            if new_pulse == "low":
                low += 1
            else:
                high += 1

            print(f"{current_module} -{new_pulse}-> {destination_module}")

            if destination_module in conjunction_names:
                conjunction_dict = update_conjunction_dict(
                    conjunction_dict, new_pulse, destination_module, current_module
                )

            queue.insert(0, (destination_module, new_pulse))

    return low, high


def count_pulses(filename, button_count) -> Tuple[int, int]:
    with open(filename) as f:
        modules_configuration = f.read().splitlines()
    modules_configuration, conjunction_dict = parse_modules(modules_configuration)
    conjunction_names = list(conjunction_dict.keys())

    total_low = 0
    total_high = 0

    for i in range(button_count):
        low, high = press_button(
            modules_configuration, conjunction_dict, conjunction_names
        )
        total_low += low
        total_high += high
    return total_low, total_high


if "__main__" == __name__:
    low, high = count_pulses("Day_20/puzzle_input.txt", button_count=1000)
    print(low * high)
