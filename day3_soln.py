import re


def part1():
    sum_of_mul_nos = 0
    with open("day3_input.txt") as file:
        for line in file:
            line = line.strip()
            number_pairs = re.findall("mul\\((\\d{0,3}),(\\d{0,3})\\)", line)
            for pair in number_pairs:
                sum_of_mul_nos += int(pair[0]) * int(pair[1])
    print(sum_of_mul_nos)


def part2():
    sum_of_mul_nos = 0
    number_pairs = []
    with open("day3_input.txt") as file:
        full_text = file.readlines(-1)
        full_text = " ".join(full_text)
    split_by_do = re.split("do\\(", full_text)
    for split_line in split_by_do:
        split_by_dont = re.split("don't\\(", split_line)[0]
        number_pairs += re.findall("mul\\((\\d{0,3}),(\\d{0,3})\\)", split_by_dont)
    for pair in number_pairs:
        sum_of_mul_nos += int(pair[0]) * int(pair[1])
    print(sum_of_mul_nos)


if __name__ == "__main__":
    part1()
    part2()
