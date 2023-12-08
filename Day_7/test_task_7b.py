from task_7b import get_hand_type, HandType, get_total_winnings, create_ranking


def test_get_hand_type():
    assert get_hand_type("QQQQ2") == HandType.FOUR_OF_A_KIND
    assert get_hand_type("QQQJ2") == HandType.FOUR_OF_A_KIND
    assert get_hand_type("JJJJJ") == HandType.FIVE_OF_A_KIND


def test_create_ranking():
    game = ["QQQQ2 100", "QQQJ2 105", "JJJJJ 44"]
    assert create_ranking(game) == [("5QQQJ2", 105), ("5QQQQ2", 100), ("6JJJJJ", 44)]


def test_get_total_winnings():
    game = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
    assert get_total_winnings(game) == 5905
