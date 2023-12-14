from task_13a import find_reflection_line, summarize_pattern_notes


class TestSummarizePatternNotes(object):
    def test_summarize_pattern_notes(self):
        assert summarize_pattern_notes("Day_13/example_13a.txt") == 405


# vertial - columns
# horizontal - rows * 100
class TestFindReflectionLine(object):
    def test_on_vertical_reflection_line(self):
        pattern_map = """
        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#.
        """
        assert find_reflection_line(pattern_map) == 5

    def test_on_horizontal_reflection_line(self):
        pattern_map = """
        #...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#
        """
        assert find_reflection_line(pattern_map) == 400

    def test_on_horizontal_reflection_line_close_to_beginning(self):
        pattern_map = """
        .##.##....##...
        .....#.#.#..#.#
        .....#.#.#..#.#
        .##.##....##...
        ..###.#.##..#.#
        #.###.#.#######
        ##..#..###.####
        """
        assert find_reflection_line(pattern_map) == 200

    def test_on_horizontal_reflection_line_at_the_end(self):
        pattern_map = """
        ..##.####
        .#....##.
        .##..#..#
        ..#.#.###
        .##..#..#
        ##.#.#..#
        ##.#.#..#
        """
        assert find_reflection_line(pattern_map) == 600

    def test_on_vertical_reflection_line_close_to_beggining(self):
        pattern_map = """
        ##..#...#.#..#.
        ##.###...###..#
        ...#.#####....#
        ..##.#####....#
        ##.###...###..#
        ##..#...#.#..#.
        ..#..###.#####.
        """
        assert find_reflection_line(pattern_map) == 1

    def test_on_few_possible_vertical_reflection_lines(self):
        pattern_map = """
        #####..
        ..####.
        ..####.
        ###.#..
        ..#....
        ###...#
        .#..##.
        ...#.##
        ...##..
        .#...#.
        .#...#.
        .######
        .######
        .#...#.
        .#...#.
        ...##..
        ...#.##
        """
        assert find_reflection_line(pattern_map) == 1200

    def test_rerewr(self):
        pattern_map = """
        ....######.
        #..###..###
        .....#..#..
        #####.##.##
        .##...##...
        ....######.
        ....##..###
        .##.#.##.#.
        .##.######.
        .##........
        ....######.
        .##..#..#..
        #..#.#..#.#
        .##.#....#.
        ####..##..#
        ....######.
        #..#..##..#
        """
        assert find_reflection_line(pattern_map) == 2
