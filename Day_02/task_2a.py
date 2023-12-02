MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def is_set_valid(game_set):
    """Check one set of cubes"""
    cubes = game_set.split(",")
    valid_game = False

    for cube in cubes:
        cube_num, cube_color = cube.strip().split(" ")
        if cube_color == "red" and int(cube_num) > MAX_RED:
            break
        if cube_color == "green" and int(cube_num) > MAX_GREEN:
            break
        if cube_color == "blue" and int(cube_num) > MAX_BLUE:
            break
    else:  # if no break happened
        valid_game = True

    return valid_game


def is_game_valid(game):
    """Check one game"""
    game = game.split(";")
    for game_set in game:
        if not is_set_valid(game_set):
            return False
    return True


def find_valid_games_ids(filename):
    valid_game_ids = []
    with open(filename, "r") as f:
        for line in f.readlines():
            game_id, game = line.split(":")
            if is_game_valid(game):
                game_id = int(game_id.split(" ")[1])  # take only number
                valid_game_ids.append(game_id)
    return valid_game_ids


if __name__ == "__main__":
    print(sum(find_valid_games_ids("Day_02/puzzle_input.txt")))
