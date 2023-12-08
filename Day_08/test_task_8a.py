from task_8a import count_steps
import pytest


@pytest.mark.parametrize(
    "test_input,expected", [("Day_08/example_8a.txt", 2), ("Day_08/example_8b.txt", 6)]
)
def test_count_step(test_input, expected):
    assert count_steps(test_input) == expected
