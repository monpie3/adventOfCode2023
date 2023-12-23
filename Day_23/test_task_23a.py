from task_23a import count_steps_to_meta


def test_count_pulses():
    filename = "Day_23/example_23a.txt"
    assert set(count_steps_to_meta(filename)) == {74, 82, 86, 90, 94}
