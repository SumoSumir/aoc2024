import pandas as pd


def part1():
    """
    Find the distance between 2 locations ID's (after sorting both lists) & return the sum of all distances
    """
    df = pd.read_csv("day1_input.csv", sep="\\s+", header=None)
    df = df.rename(columns={0: "list1", 1: "list2"})
    df["list1"] = df["list1"].sort_values(ignore_index=True)
    df["list2"] = df["list2"].sort_values(ignore_index=True)
    df["distance"] = (df["list1"] - df["list2"]).abs()
    print("Sum of the distances is: ", df["distance"].sum())
    part2(df)


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
