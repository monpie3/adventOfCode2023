from task_1b import extract_from_line

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("eighthree ", 83),
    ],
)
def test_find_calibration_values(test_input, expected):
    assert extract_from_line(test_input) == expected
