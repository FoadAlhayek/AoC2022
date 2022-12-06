#!/usr/bin/env python
# @Author: Foad Alhayek (a448431)
# @Filename: day_04.py
# @Date: 2022-12-05
# @Description: My simple implementation of the Advent of Code daily challenge, the code is not to be considered 
#               optimized nor the best, but instead a fun first-hand implementation done rather quickly or experimenting
#               with Python. Some solutions are over the top due to me trying different ways to solve the task.

# Fully contained pair counter and "overlap at all" counter
full_pair_counter = 0
overlap_counter = 0

with open("data/day_04.txt", "r", encoding="utf-8") as fid:
    for line in fid:
        # [[min_1, max_1], [min_2, max_2]]
        elf_one, elf_two = [list(map(int, x.split('-'))) for x in line.split(',')]

        # Flags needed because I didn't feel like separating Part 1 and 2 otherwise "continue" would have been used
        part_one_found = False
        part_two_found = False

        if elf_one[0] <= elf_two[0]:
            # Part 1
            if elf_one[1] >= elf_two[1]:
                full_pair_counter += 1
                part_one_found = True
                # continue

            # Part 2 - Sufficient if max of elf one is bigger than min of elf two
            if elf_one[1] >= elf_two[0]:
                overlap_counter += 1
                part_two_found = True
                # continue

        if elf_two[0] <= elf_one[0] and not part_one_found:
            # Part 1
            if elf_two[1] >= elf_one[1]:
                full_pair_counter += 1

            # Part 2
            if elf_two[1] >= elf_one[0] and not part_two_found:
                overlap_counter += 1

print(f"Part 1; Fully contained pairs: {full_pair_counter}")
print(f"Part 2; Any overlap pairs: {overlap_counter}")
