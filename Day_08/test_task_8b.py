import pytest
from task_8b import count_min_steps


def test_count_min_steps():
    assert count_min_steps("Day_08/example_8c.txt") == 6
