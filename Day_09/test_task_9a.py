from task_9a import extrapolate_history


class TestExtrapolateHistory(object):
    def test_on_values_incresead_by_the_same_step(self):
        assert extrapolate_history("0 3 6 9 12 15") == 18

    def test_on_values_incresead_by_the_diffrent_step(self):
        assert extrapolate_history("1 3 6 10 15 21") == 28
        assert extrapolate_history("10 13 16 21 30 45") == 68

    def test_on_negative_values(self):
        assert extrapolate_history("-15 -12 -9 -6 -3 0") == 3
