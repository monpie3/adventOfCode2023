import pandas as pd


def parse_map(map_str):
    lines = map_str.split("\n")[1:]  # omit the first line
    return [list(map(int, line.split())) for line in lines]


def find_corespond(value_to_tranlate, maps_with_translation):
    for map_values in maps_with_translation:
        destination_range_start, source_range_start, range_length = map_values
        if (
            value_to_tranlate >= source_range_start
            and value_to_tranlate <= range_length + source_range_start
        ):
            diffrence = value_to_tranlate - source_range_start
            translation = destination_range_start + diffrence
            return translation
    return value_to_tranlate


if "__main__" == __name__:
    with open("Day_05/puzzle_input.txt") as f:
        file_content = f.read()

    maps = file_content.strip().split("\n\n")
    seeds = maps[0].split("seeds:")[1].strip().split(" ")
    seeds = list(map(int, seeds))

    df = pd.DataFrame(seeds, columns=["seeds"])

    map_categories = [
        "seeds",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ]
    for ind, map_str in enumerate(maps[1:]):
        map_category = parse_map(map_str)
        source = map_categories[ind]
        destination = map_categories[ind + 1]
        df[destination] = df[source].apply(
            lambda x: find_corespond(int(x), map_category)
        )

    print(df)
    print(df[df.location == df.location.min()])
