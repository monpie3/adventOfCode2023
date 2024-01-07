import pandas as pd


def expand_galaxy(galaxy):
    """any rows or columns that contain no galaxies
    should all actually be x-times bigger

    add rows and columns with the letter "E" to indicate where the map should expand
    """
    new_row = ["E"] * len(galaxy[0])

    # go by rows
    rows_to_duplicate = [ind for ind, row in enumerate(galaxy) if "#" not in row]

    # insert rows from the last index - this way indices above are not affected
    for row_ind in rows_to_duplicate[::-1]:
        galaxy.insert(row_ind, new_row)

    galaxy = pd.DataFrame(galaxy)

    # go by columns
    col_to_duplicate = galaxy.columns[(galaxy != "#").all(axis=0)]

    # old version
    # col_to_duplicate = [col_ind for col_ind in range(len(galaxy.columns)) if "#" not in list(galaxy[:][col_ind])]
    # "#" not in list(galaxy[:][col_ind])
    # is not the same as
    # "#" not in galaxy[:][col_ind]

    # insert columns from the last index - this way indices above are not affected
    for col_ind in col_to_duplicate[::-1]:
        galaxy.insert(col_ind, "tmp", value="E", allow_duplicates=True)

    galaxy.set_axis(range(galaxy.shape[1]), axis=1)
    galaxy = galaxy.T.reset_index(drop=True).T  # reset column names
    return pd.DataFrame(galaxy)


def process_input(filename):
    with open(filename) as f:
        file_content = f.read()

    image = [list(line) for line in file_content.split()]
    return image


def find_indecies_of_galaxies(image):
    # Use stack() to transform the DataFrame into a Series
    # and reset_index() to add the index as a column
    df_stacked = image.stack().reset_index()

    # Find indices for '#'
    galaxies_indecies = df_stacked[df_stacked[0] == "#"][:].iloc[:, :-1].values
    # With iloc[:,:-1] we remove the last column which is '#'
    return list(map(tuple, galaxies_indecies))


def find_number_of_steps(galaxies_indecies, galaxy_map, times):
    diffrence_between = []
    for ind, galaxy_index in enumerate(galaxies_indecies):
        row_num, col_num = galaxy_index

        for ind_2 in range(ind + 1, len(galaxies_indecies)):
            row_num_1, col_num_1 = row_num, col_num
            row_num_2, col_num_2 = galaxies_indecies[ind_2]

            if row_num_1 > row_num_2:
                row_num_1, row_num_2 = row_num_2, row_num_1

            if col_num_1 > col_num_2:
                col_num_1, col_num_2 = col_num_2, col_num_1

            path_to_one_galaxy_to_another = galaxy_map.loc[
                row_num_1:row_num_2, col_num_1:col_num_2
            ]

            # count how many rows and columns should be inserted
            num_inserted_columns = len(
                path_to_one_galaxy_to_another.columns[
                    (path_to_one_galaxy_to_another == "E").all()
                ]
            )
            num_inserted_rows = len(
                path_to_one_galaxy_to_another.index[
                    (path_to_one_galaxy_to_another == "E").all(axis=1)
                ]
            )

            # take into account counting distance between galaxies
            diffrence_between_rows = (
                row_num_2 - row_num_1 + num_inserted_rows * (times - 2)
            )
            diffrence_between_cols = (
                col_num_2 - col_num_1 + num_inserted_columns * (times - 2)
            )
            # -2 because we already have one row/column which we want to expand
            # and we also added one row/column in the expand_galaxy function

            shortest_path = diffrence_between_rows + diffrence_between_cols
            diffrence_between.append(shortest_path)

    return diffrence_between


def find_shortest_path_between_galaxies(filename, multiplier=2):
    image = process_input(filename)
    galaxy_map = expand_galaxy(image)
    galaxies_indecies = find_indecies_of_galaxies(galaxy_map)
    return find_number_of_steps(galaxies_indecies, galaxy_map, multiplier)


if "__main__" == __name__:
    print(
        sum(
            find_shortest_path_between_galaxies(
                "Day_11/puzzle_input.txt", multiplier=1000000
            )
        )
    )
