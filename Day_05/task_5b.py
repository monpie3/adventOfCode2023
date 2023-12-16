import pandas as pd
from typing import List


def process_input(filename):
    with open(filename) as f:
        seeds, *translations_maps = f.read().split("\n\n")

    seeds = seeds.split("seeds:")[1]
    seeds = list(map(int, seeds.split()))

    seeds_list = []
    for i in range(0, len(seeds), 2):
        seeds_list.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
        # because we are including a start value in range, we need to substract 1

    almanac = pd.DataFrame(seeds_list, columns=["seeds_min", "seeds_max"])
    return almanac, translations_maps


def parse_map(map_str: str) -> List:
    """Parse a translation map string into a list of tuples.

    Args:
        map_str: unprocessed trasnalation map

    Returns:
        list of tuples (destination_range_start, source_range_start, range_length)
    """
    lines = map_str.strip().split("\n")[1:]  # omit the 1st line, which is a map header
    return [tuple(map(int, line.split())) for line in lines]


def find_edges(translation_map: List) -> List:
    """Find all potential edge points in a translation map.

    Args:
        translation_map: list of tuples (destination_range_start, source_range_start, range_length)

    Returns:
        a sorted list of potential edge points
    """
    edges = []
    for map_values in translation_map:
        _, source_range_start, range_length = map_values
        edges.append((source_range_start))
        edges.append((source_range_start + range_length - 1))
        # because we are including a start value in range, we need to substract 1
    return sorted(edges)


def split_by_edge(
    almanac: pd.DataFrame, edges: List, category_name: str
) -> pd.DataFrame:
    """Split source ranges by edges.
    This way we can translate ranges that are not fully included in a single destination range.

    Args:
        almanac: a dataframe with ranges to be translated
        edges: a sorted list of potential edge points
        category_name: name of the category from which we translate

    Returns:
        a dataframe with new ranges, taking into account the edges

    """
    current_source_min = almanac[f"{category_name}_min"]
    current_source_max = almanac[f"{category_name}_max"]
    new_points = []
    for ind in range(len(almanac)):
        for edge in edges:
            if current_source_min[ind] < edge < current_source_max[ind]:
                new_range = pd.Series(
                    {
                        f"{category_name}_min": edge + 1,
                        f"{category_name}_max": current_source_max[ind],
                    }
                )
                # add new range
                new_points.append(new_range)

                # update previous point
                almanac.at[ind, f"{category_name}_max"] = edge

    # update almanac with new ranges
    if len(new_points) > 0:
        almanac_2 = pd.DataFrame(new_points)
        almanac = pd.concat([almanac, almanac_2], axis=0)
        almanac = almanac.reset_index(drop=True)
    return almanac


def translate(value_to_translate: int, translation_map: List) -> int:
    """Translate a value from one category to another.

    Args:
        value_to_translate: value to be translated
        translation_map: list of tuples (destination_range_start, source_range_start, range_length)

    Returns:
        translated value
    """
    for map_values in translation_map:
        destination_range_start, source_range_start, range_length = map_values
        if (
            value_to_translate >= source_range_start
            and value_to_translate < range_length + source_range_start
        ):
            diffrence = destination_range_start - source_range_start
            translation = value_to_translate + diffrence
            return translation
    return value_to_translate


def create_almanac(filename):
    almanac, translations_maps = process_input(filename)

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

    for m_ind, map_str in enumerate(translations_maps):
        translation_map = parse_map(map_str)
        edges = find_edges(translation_map)
        category_name = map_categories[m_ind]
        almanac = split_by_edge(almanac, edges, category_name)

        destination_name = map_categories[m_ind + 1]

        almanac[f"{destination_name}_min"] = almanac[f"{category_name}_min"].apply(
            lambda x: translate(int(x), translation_map)
        )

        if destination_name != "location":
            almanac[f"{destination_name}_max"] = almanac[f"{category_name}_max"].apply(
                lambda x: translate(int(x), translation_map)
            )
    return almanac


if "__main__" == __name__:
    almanac = create_almanac("Day_05/puzzle_input.txt")
    print(almanac[almanac.location_min == almanac.location_min.min()])
