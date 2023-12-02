from task_2a import is_game_valid

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
        ("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
        ("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", False),
        ("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", False),
        ("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),
    ],
)
def test_is_game_valid(test_input, expected):
    assert is_game_valid(test_input) == expected
