#!/usr/bin/env python
# @Author: Foad Alhayek (a448431)
# @Filename: day_01.py
# @Date: 2022-12-01
# @Description: My simple implementation of the Advent of Code daily challenge, the code is not to be considered
#               optimized nor the best, but instead a fun first-hand implementation done rather quickly or experimenting
#               with Python. Some solutions are over the top due to me trying different ways to solve the task.
import numpy as np

# Part 1, find max value - Part 2, sum max-top 3 values
with open("data/day_01.txt", 'r', encoding='utf-8') as fid:
    elf_max_3 = np.zeros(3)
    elf_cal = 0

    # Loop over the data and sum up every elf's calories
    for line in fid:
        if line == '\n':
            if elf_cal > elf_max_3[0]:
                elf_max_3[0] = elf_cal
            elif elf_cal > elf_max_3[1]:
                elf_max_3[1] = elf_cal
            elif elf_cal > elf_max_3[2]:
                elf_max_3[2] = elf_cal

            elf_cal = 0
            continue

        elf_cal += float(line)

    # Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    print(f"Part 1, Max cal: {np.max(elf_max_3)}")

    # Sum of top 3 Elf's
    print(f"Part 2, Top 3 sum: {np.sum(elf_max_3)}")


