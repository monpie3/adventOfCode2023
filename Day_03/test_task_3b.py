import math
from task_3b import find_gear_ratio


def test_find_calibration_values():
    gears = find_gear_ratio("Day_03/example_3b.txt")
    gear_ratio = []
    for key in gears.keys():
        if len(gears[key]) > 1:
            gear_ratio.append(math.prod(gears[key]))

    assert sum(gear_ratio) == 467835
