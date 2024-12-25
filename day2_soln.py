import pandas as pd
import re


def order_check(row: list):
    """
    Checks if all the elements in a row are all gradually ascending/descending
    At most difference of 1, and at least of 3 between the elements are permitted
    """
    row_order_check = []
    for index in range(0, len(row) - 1):
        if row[index] < row[index + 1]:
            row_order_check.append(True)
        else:
            row_order_check.append(False)

    return all(row_order_check) or not any(row_order_check)


def step_check(row: list):
    for index in range(0, len(row) - 1):
        if row[index] - row[index + 1] not in [1, 2, 3, -1, -2, -3]:
            return False
    return True


def part1():
    """
    Check levels of reactor
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    # # No. of columns are not consistent through out the file (separator not present for all cols)
    # # Wanted to explore pandas/dataframe more but read_csv is not the best for the problem

    # df = pd.read_csv(
    #     "day2_input.csv",
    #     sep="\\s+",
    #     header=None,
    #     usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    #     na_values=None,
    # )

    count = 0

    # Was experimenting with "assignment" inside lambdas - Doesn't work
    # is_ordered_lambda = lambda row: (
    #     row_order_result := [
    #         True if row[index] < row[index + 1] else False
    #         for index in range(0, len(row) - 1)
    #     ]
    #     and ( all(row_order_result)
    #     or not any(row_order_result)
    #     )
    # )

    with open("day2_input.csv") as file:
        for row in file:
            row = re.split("\\s+", row.strip())
            row = [int(i) for i in row]
            # Didn't have to break it into 2 functions/loops - but its cleaner this way
            if order_check(row) and step_check(row):
                count += 1
    print(count)


def part2(df: pd.DataFrame):
    """
    Find elements in list1 present in list2 & multiply them with its no. of occurences
    """
    df["list1_occurrences"] = df["list1"].apply(lambda id: df["list2"].isin([id]).sum())
    print(
        "Common no.s * no. of occurences = ",
        (df["list1"] * df["list1_occurrences"]).sum(),
    )


if __name__ == "__main__":
    part1()
