from task_11b import find_shortest_path_between_galaxies


def test_find_calibration_values():
    filename = "Day_11/example_11a.txt"
    assert sum(find_shortest_path_between_galaxies(filename, 2)) == 374
    assert sum(find_shortest_path_between_galaxies(filename, 10)) == 1030
    assert sum(find_shortest_path_between_galaxies(filename, 100)) == 8410
