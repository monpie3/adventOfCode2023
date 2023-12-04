import re
from collections import defaultdict


def count_winning_numbers_matches(card):
    """Check how many winning numbers are on the card"""
    card = re.sub(" +", " ", card)
    winning_nums, current_nums = card.split("|")
    winning_nums = winning_nums.strip().split(" ")
    current_nums = current_nums.strip().split(" ")
    return len(set(winning_nums) & set(current_nums))


def win_copies(filename):
    total_cards = defaultdict(lambda: {"original": 0, "copy": 0})

    with open(filename, "r") as f:
        for line in f.readlines():
            card_id, numbers_to_check = line.split(":")
            card_id = int(card_id.split(" ")[-1])

            # go through orginal cards
            total_cards[card_id]["original"] = 1

            num_of_new_cards = count_winning_numbers_matches(numbers_to_check)

            # add copies
            # if there is not only original card but also a copy we add more cards
            how_many_copies = 1 + total_cards[card_id]["copy"]

            for ind in range(1, num_of_new_cards + 1):
                card_id_to_copy = card_id + ind
                total_cards[card_id_to_copy]["copy"] += how_many_copies

    return total_cards


def get_number_of_copies(filename):
    cards = win_copies(filename)
    total_number = 0
    for card_amount in cards.values():
        total_number += card_amount["original"]
        total_number += card_amount["copy"]
    return total_number


if __name__ == "__main__":
    print(get_number_of_copies("Day_04/puzzle_input.txt"))
