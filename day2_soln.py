import pandas as pd
import re
from collections import Counter


def order_check_elem(elem1: int, elem2: int):
    if elem1 < elem2:
        order = "ascending"
    elif elem1 > elem2:
        order = "descending"
    else:
        order = "same"
    return order


def step_check_elem(elem1: int, elem2: int):
    if elem1 - elem2 in [1, 2, 3, -1, -2, -3]:
        return True
    return False


def level_check(row: list, allowed_failures: int):

    if allowed_failures < 0:
        return False

    order_list = [order_check_elem(row[i], row[i + 1]) for i in range(0, len(row) - 1)]
    most_common_order = Counter(order_list).most_common(1)

    if (len(row) - 1) - most_common_order[0][1] > 1 or most_common_order[0][
        0
    ] == "same":
        return False

    for index in range(0, len(row) - 1):
        if (
            not step_check_elem(row[index], row[index + 1])
            or order_check_elem(row[index], row[index + 1]) != most_common_order[0][0]
        ):
            allowed_failures -= 1
            row_without_index = row[:index] + row[index + 1 :]
            row_without_element_above_index = row[: index + 1] + row[index + 2 :]
            result = level_check(row_without_index, allowed_failures) or level_check(
                row_without_element_above_index, allowed_failures
            )
            return result

    return True


def part1_and_2():
    """
    Check levels of reactor
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    count = 0
    with open("day2_input.csv") as file:
        for row in file:
            row = re.split("\\s+", row.strip())
            row = [int(i) for i in row]
            if level_check(row, 1):
                count += 1
    print(count)


if __name__ == "__main__":
    part1_and_2()
