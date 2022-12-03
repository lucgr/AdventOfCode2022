def method():
    file = open("input/input3.txt", "r")
    sum1, sum2, iter, group = 0, 0, 1, []  # initial variable assignment
    for line in file:
        ### PART 1 ###
        compartment_1 = line[: len(line) // 2]
        compartment_2 = line[len(line) // 2 :]
        common_item = list(set(compartment_1) & set(compartment_2))
        sum1 += find_value(char=common_item[0])

        ### PART 2 ###
        group.append(line)
        if iter % 3 == 0:  # make groups of 3
            badge = find_common_item(bags=group)
            sum2 += find_value(char=badge)
            group = []
        iter += 1
    print(f"Part 1 - Sum: {sum1}")
    print(f"Part 2 - Sum: {sum2}")


def find_value(char: str):
    if char.islower():
        return ord(char) - 96  # lowercase, ascii-value minus 96 to start at 1
    return ord(char) - 38  # uppercase, ascii-value minus 38 to start at 27


def find_common_item(bags: list):
    bags = [bag[:-1] for bag in bags]
    common_item = list(set(bags[0]) & set(bags[1]) & set(bags[2]))[0]
    return common_item


if __name__ == "__main__":
    method()
