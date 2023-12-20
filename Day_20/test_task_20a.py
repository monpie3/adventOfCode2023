from task_20a import count_pulses


def test_count_pulses():
    assert count_pulses("Day_20/example_20a.txt", button_count=1) == (8, 4)
    assert count_pulses("Day_20/example_20a.txt", button_count=1000) == (8000, 4000)

    assert count_pulses("Day_20/example_20b.txt", button_count=1) == (4, 4)
    assert count_pulses("Day_20/example_20b.txt", button_count=1000) == (4250, 2750)
