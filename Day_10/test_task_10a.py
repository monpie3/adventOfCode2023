from task_10a import get_step_number


def test_find_calibration_values():
    assert get_step_number("Day_10/example_10a.txt") == 4
    assert get_step_number("Day_10/example_10b.txt") == 8
