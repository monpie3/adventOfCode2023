from task_1a import find_calibration_values


def test_find_calibration_values():
    assert find_calibration_values("Day_01/example.txt") == [12, 38, 15, 77]
