from task_10b import count_enclosed_tiles


def test_count_enclosed_tiles():
    assert count_enclosed_tiles("Day_10/example_10a.txt") == 1
    assert count_enclosed_tiles("Day_10/example_10b.txt") == 1
    assert count_enclosed_tiles("Day_10/example_10c.txt") == 4
    assert count_enclosed_tiles("Day_10/example_10d.txt") == 8
    assert count_enclosed_tiles("Day_10/example_10e.txt") == 10
