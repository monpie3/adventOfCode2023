from task_12a import get_num_of_possible_arrangements


def test_get_num_of_possible_arrangements():
    assert get_num_of_possible_arrangements("???.###", "1,1,3") == 1
    assert get_num_of_possible_arrangements(".??..??...?##.", "1,1,3") == 4
    assert get_num_of_possible_arrangements("?#?#?#?#?#?#?#?", "1,3,1,6") == 1
    assert get_num_of_possible_arrangements("????.#...#...", "4,1,1") == 1
    assert get_num_of_possible_arrangements("????.######..#####.", "1,6,5") == 4
    assert get_num_of_possible_arrangements("?###????????", "3,2,1") == 10
