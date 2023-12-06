from task_5a import find_corespond

import pytest


@pytest.mark.parametrize(
    "source,expected",
    [(79, 81), (14, 14), (55, 57), (13, 13)],
)
def test_find_correspond(source, expected):
    map_with_translation = [[50, 98, 2], [52, 50, 48]]
    destination_category = find_corespond(source, map_with_translation)
    assert destination_category == expected
