from task_3a import find_part_numbers, evaluate_engine_schematic


class TestFindPartNumbers(object):
    def test_find_part_numbers(self):
        assert sum(find_part_numbers("Day_03/example_3a.txt")) == 4361


class TestEvaluateEngineSchematic(object):
    def test_on_number_on_edge(self):
        schematic = [
            ".....+.58.........58........58.......*58........58....*",
            "..712.996.................646.40...1.....875..958...553",
            "3............698.239...............*...................",
        ]
        assert evaluate_engine_schematic(schematic) == [58, 712, 996, 1, 553]

    def test_on_subnumber(self):
        # number 1 is part of number 712
        schematic = [
            "..712.996.................646.40...1.....875..958.553..",
            "3............698.239.........*.....*.............*.....",
        ]
        assert evaluate_engine_schematic(schematic) == [646, 40, 1, 958, 553]

    def test_on_same_number_twice_in_row(self):
        schematic = [
            ".....+.58........*58........58.......*58......+.58.....",
            "..712.996.................646.40...1.....875..958.553..",
            "3............698.239...............*...................",
        ]
        assert evaluate_engine_schematic(schematic) == [58, 58, 712, 996, 1, 958]

    def test_on_single_row(self):
        schematic = ["617*...66..."]
        assert evaluate_engine_schematic(schematic) == [617]

    def test_schematic_without_numbers(self):
        schematic = ["............", "............"]
        assert evaluate_engine_schematic(schematic) == []

    def test_schematic_with_only_asterisks(self):
        schematic = ["***.***.***"]
        assert evaluate_engine_schematic(schematic) == []
