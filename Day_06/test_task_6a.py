from task_6a import count_ways_to_win


def test_count_ways_to_win():
    assert count_ways_to_win((7, 9)) == 4
    assert count_ways_to_win((15, 40)) == 8
    assert count_ways_to_win((30, 200)) == 9
