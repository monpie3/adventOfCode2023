import math


def count_ways_to_win(record):
    time, min_distance = record
    num_of_ways_per_race = 0
    for t in range(time):
        speed = t
        distance = speed * (time - t)
        if distance > min_distance:
            num_of_ways_per_race += 1
        if num_of_ways_per_race > 1 and distance < min_distance:
            # we reach peak, no more ways to win
            break
    return num_of_ways_per_race


def parse_input(file_content):
    time = map(int, file_content[0].split(":")[1].split())
    min_distance = map(int, file_content[1].split(":")[1].split())
    return [(t, d) for t, d in zip(time, min_distance)]


if "__main__" == __name__:
    with open("Day_06/puzzle_input.txt") as f:
        file_content = f.readlines()

    sheetOfPaper = parse_input(file_content)
    num_of_ways = []
    for record in sheetOfPaper:
        num_of_ways.append(count_ways_to_win(record))

    print("Answer:", math.prod(num_of_ways))
