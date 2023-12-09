from task_9b import extrapolate_backwards


class TestExtrapolateHistory(object):
    def test_on_values_incresead_by_the_same_step(self):
        assert extrapolate_backwards("0 3 6 9 12 15") == -3

    def test_on_values_incresead_by_the_diffrent_step(self):
        assert extrapolate_backwards("1 3 6 10 15 21") == 0
        assert extrapolate_backwards("10 13 16 21 30 45") == 5

    def test_on_negative_values(self):
        assert extrapolate_backwards("-15 -12 -9 -6 -3 0") == -18
