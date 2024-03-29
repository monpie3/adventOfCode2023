from collections import Counter
from enum import Enum


class HandType(Enum):
    HIGH_CARD = "0"
    ONE_PAIR = "1"
    TWO_PAIRS = "2"
    THREE_OF_A_KIND = "3"
    FULL_HOUSE = "4"
    FOUR_OF_A_KIND = "5"
    FIVE_OF_A_KIND = "6"


def get_hand_type(hand):
    counted_cards = Counter(hand)
    diffrent_cards = len(counted_cards)

    if diffrent_cards == 5:
        return HandType.HIGH_CARD
    if diffrent_cards == 4:
        return HandType.ONE_PAIR
    if diffrent_cards == 1:
        return HandType.FIVE_OF_A_KIND
    if diffrent_cards == 3:
        if sorted(counted_cards.values()) == [1, 1, 3]:
            return HandType.THREE_OF_A_KIND
        return HandType.TWO_PAIRS
    if diffrent_cards == 2:
        if sorted(counted_cards.values()) == [2, 3]:
            return HandType.FULL_HOUSE
        return HandType.FOUR_OF_A_KIND


def create_ranking(games):
    type_ranking = []
    for game in games:
        hand, bind = game.split(" ")
        type = get_hand_type(hand)
        type_ranking.append((type.value + hand, int(bind)))

    return sorted(
        type_ranking, key=lambda x: x[0].translate(str.maketrans("TJQKA", f"ABCDE"))
    )


def get_total_winnings(file_content):
    ranking = create_ranking(file_content)
    winnings = sum([ind * ranking[ind - 1][1] for ind in range(1, len(ranking) + 1)])
    return winnings


if "__main__" == __name__:
    with open("Day_07/puzzle_input.txt") as f:
        file_content = f.read().splitlines()
    print(get_total_winnings(file_content))
