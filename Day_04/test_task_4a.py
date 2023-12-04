from task_4a import (
    calculate_total_points,
    count_winning_numbers_matches,
    get_scratchcard_value,
)


class TestCalculateTotalPoints(object):
    def test_calculate_total_points(self):
        assert calculate_total_points("Day_04/example_4a.txt") == 13


class TestCountWinningNumbersMatches(object):
    def test_on_valid_value(self):
        card = "41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        assert count_winning_numbers_matches(card) == 4
        assert get_scratchcard_value(4) == 8

    def test_on_zero_winning_numbers(self):
        card = "41 48 83 86 17 | 1 2 3 4 5 6 7 8"
        assert count_winning_numbers_matches(card) == 0
        assert get_scratchcard_value(0) == 0
