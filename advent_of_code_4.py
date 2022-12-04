def method():
    file = open("input/input4.txt", "r")
    overlaps_1 = 0
    overlaps_2 = 0
    for line in file:
        ### SETUP ###
        elf_1, elf_2 = line.split(",")[0], line.split(",")[1]
        e1_range = range(int(elf_1.split("-")[0]), int(elf_1.split("-")[1]) + 1)
        e2_range = range(int(elf_2.split("-")[0]), int(elf_2.split("-")[1]) + 1)

        ### PART 1 ###
        is_overlap = all(e in e2_range for e in e1_range) or all(e in e1_range for e in e2_range)
        if is_overlap:
            overlaps_1 += 1

        ### PART 2 ###
        if len(set(e1_range).intersection(set(e2_range))) > 0:
            overlaps_2 += 1

    print(f"Part 1 - Complete overlaps: {overlaps_1}")
    print(f"Part 2 - Partial overlaps: {overlaps_2}")


if __name__ == "__main__":
    method()
