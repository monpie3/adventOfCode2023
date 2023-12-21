from task_21a import count_garden_plots


def test_count_pulses():
    assert count_garden_plots("Day_21/example_21a.txt", step_limit=1) == 2
    assert count_garden_plots("Day_21/example_21a.txt", step_limit=2) == 4
    assert count_garden_plots("Day_21/example_21a.txt", step_limit=3) == 6
    assert count_garden_plots("Day_21/example_21a.txt", step_limit=6) == 16
