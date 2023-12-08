from task_8a import count_steps, go_right, go_left
import pytest


@pytest.mark.parametrize("test_input,expected", [("Day_8/example_8a.txt", 2), ("Day_8/example_8b.txt", 6)])
def test_count_step(test_input, expected):
    assert count_steps(test_input) == expected
