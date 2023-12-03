from collections import defaultdict
import math


def find_minimum_set_of_cubes(game):
    game = game.split(";")

    min_set_of_cubes = defaultdict(int)

    for game_set in game:
        cubes = game_set.split(",")
        for cube in cubes:
            cube_num, cube_color = cube.strip().split(" ")
            if min_set_of_cubes[cube_color] < int(cube_num):
                min_set_of_cubes[cube_color] = int(cube_num)
    return min_set_of_cubes


def find_power_of_set_of_cubes(filename):
    sets_power = []
    with open(filename, "r") as f:
        for line in f.readlines():
            game_id, game = line.split(":")
            min_set_of_cubes = find_minimum_set_of_cubes(game)
            result = math.prod(min_set_of_cubes.values())
            sets_power.append(result)
    return sets_power


if __name__ == "__main__":
    print(sum(find_power_of_set_of_cubes("Day_02/puzzle_input.txt")))
