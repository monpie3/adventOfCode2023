from task_24a import count_intersection


def test_count_steps_to_meta():
    min_window = 7
    max_window = 27

    assert count_intersection("Day_24/example_24a.txt", min_window, max_window) == 2
