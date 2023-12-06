def count_ways_to_win(record):
    time, min_distance = record
    num_of_ways_per_race = 0
    for hold_time in range(time):
        speed = hold_time
        distance = speed * (time - hold_time)
        if distance > min_distance:
            num_of_ways_per_race += 1
        elif num_of_ways_per_race > 1:
            # no more ways to win
            break
    return num_of_ways_per_race


def parse_input(file_content):
    time = file_content[0].split(":")[1].split()
    time = "".join(time)
    min_distance = file_content[1].split(":")[1].split()
    min_distance = "".join(min_distance)
    return (int(time), int(min_distance))


if "__main__" == __name__:
    with open("Day_06/puzzle_input.txt") as f:
        file_content = f.readlines()

    sheetOfPaper = parse_input(file_content)
    num_of_ways = count_ways_to_win(sheetOfPaper)

    print("Answer:", num_of_ways)
