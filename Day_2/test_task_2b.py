from task_2b import find_minimum_set_of_cubes

import math
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
        ("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
        ("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
        ("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
        ("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
    ],
)
def test_is_game_valid(test_input, expected):
    min_set_of_cubes = find_minimum_set_of_cubes(test_input)
    result = math.prod(min_set_of_cubes.values())
    assert result == expected
