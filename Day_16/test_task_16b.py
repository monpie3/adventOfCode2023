from task_16b import get_num_of_energized_titles


def test_get_num_of_energized_titles():
    assert max(get_num_of_energized_titles("Day_16/example_16a.txt")) == 51
