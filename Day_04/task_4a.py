import re


def get_scratchcard_value(winning_numbers_quantity):
    """Calculate the value of the scratchcard"""
    if winning_numbers_quantity == 0:
        return 0
    return 2 ** (winning_numbers_quantity - 1)


def count_winning_numbers_matches(card):
    """Check how many winning numbers are on the card"""
    card = re.sub(" +", " ", card)
    winning_nums, current_nums = card.split("|")
    winning_nums = winning_nums.strip().split(" ")
    current_nums = current_nums.strip().split(" ")
    return len(set(winning_nums) & set(current_nums))


def count_points_on_card(card):
    """Check one card"""
    winning_numbers_quantity = count_winning_numbers_matches(card)
    return get_scratchcard_value(winning_numbers_quantity)


def calculate_total_points(filename):
    total_points = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            card_id, numbers_to_check = line.split(":")
            total_points += count_points_on_card(numbers_to_check)
    return total_points


if __name__ == "__main__":
    print((calculate_total_points("Day_04/puzzle_input.txt")))
