from task_7a import get_hand_type, HandType, get_total_winnings


def test_get_hand_type():
    assert get_hand_type("32T3K") == HandType.ONE_PAIR
    assert get_hand_type("T55J5") == HandType.THREE_OF_A_KIND
    assert get_hand_type("KK677") == HandType.TWO_PAIRS
    assert get_hand_type("KTJJT") == HandType.TWO_PAIRS
    assert get_hand_type("QQQJA") == HandType.THREE_OF_A_KIND

    assert get_hand_type("AAAAA") == HandType.FIVE_OF_A_KIND
    assert get_hand_type("AA8AA") == HandType.FOUR_OF_A_KIND
    assert get_hand_type("23332") == HandType.FULL_HOUSE
    assert get_hand_type("TTT98") == HandType.THREE_OF_A_KIND
    assert get_hand_type("23432") == HandType.TWO_PAIRS
    assert get_hand_type("A23A4") == HandType.ONE_PAIR
    assert get_hand_type("23456") == HandType.HIGH_CARD


def test_get_total_winnings():
    game = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
    assert get_total_winnings(game) == 6440
