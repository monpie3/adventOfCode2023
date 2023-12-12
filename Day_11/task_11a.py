import pandas as pd


def expand_galaxy(galaxy):
    """any rows or columns that contain no galaxies
    should all actually be twice as big"""

    # go by rows
    rows_num = len(galaxy)
    rows_to_duplicate = []
    for row_num in range(rows_num):
        if set(galaxy[row_num]) == set("."):
            rows_to_duplicate.append(row_num)
    for row_num in rows_to_duplicate[::-1]:
        galaxy.insert(row_num, galaxy[row_num])

    galaxy = pd.DataFrame(galaxy)

    # go by columns
    cols_num = len(galaxy.columns)
    col_to_duplicate = []
    for col_num in range(cols_num):
        if set(galaxy[:][col_num]) == set("."):
            col_to_duplicate.append(col_num)

    for col_num in col_to_duplicate[::-1]:
        galaxy.insert(col_num, "new_col", value=galaxy[col_num], allow_duplicates=True)

    galaxy.set_axis(range(galaxy.shape[1]), axis=1)
    galaxy = galaxy.T.reset_index(drop=True).T
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
    galaxies_indecies = df_stacked[df_stacked[0] == "#"][:].values
    return galaxies_indecies


def find_number_of_steps(galaxies_indecies):
    diffrence_between = []
    for ind, galaxy_index in enumerate(galaxies_indecies):
        row_num, col_num, _ = galaxy_index

        for ind_2 in range(ind + 1, len(galaxies_indecies)):
            row_num_2, col_num_2, _ = galaxies_indecies[ind_2]
            diffrence_between_rows = abs(row_num_2 - row_num)
            diffrence_between_cols = abs(col_num_2 - col_num)
            shortest_path = diffrence_between_rows + diffrence_between_cols
            diffrence_between.append(shortest_path)
    return diffrence_between


def find_shortest_path_between_galaxies(filename):
    image = process_input(filename)
    df = expand_galaxy(image)
    galaxies_indecies = find_indecies_of_galaxies(df)
    return find_number_of_steps(galaxies_indecies)


if "__main__" == __name__:
    print(sum(find_shortest_path_between_galaxies("Day_11/puzzle_input.txt")))
