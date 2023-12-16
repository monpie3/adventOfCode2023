from task_5b import translate, create_almanac

import pytest


@pytest.mark.parametrize(
    "source,expected",
    [(79, 81), (14, 14), (55, 57), (13, 13)],
)
def test_find_correspond(source, expected):
    translation_map = [[50, 98, 2], [52, 50, 48]]
    destination_category = translate(source, translation_map)
    assert destination_category == expected


def test_create_almanac():
    almanac = create_almanac("Day_05/example_5a.txt")
    min_location = almanac[almanac.location_min == almanac.location_min.min()]
    assert min(min_location.location_min) == 46
