from task_11a import find_shortest_path_between_galaxies


def test_find_calibration_values():
    assert sum(find_shortest_path_between_galaxies("Day_11/example_11a.txt")) == 374
