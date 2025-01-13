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



if __name__ == "__main__":
    part1()

