#!/usr/bin/env python
# @Author: Foad Alhayek (a448431)
# @Filename: day_05.py
# @Date: 2022-12-05
# @Description: My simple implementation of the Advent of Code daily challenge, the code is not to be considered 
#               optimized nor the best, but instead a fun first-hand implementation done rather quickly or experimenting
#               with Python. Some solutions are over the top due to me trying different ways to solve the task.
import numpy as np
from collections import deque, defaultdict
import re
import copy

with open("data/day_05.txt", "r", encoding="utf-8") as fid:
    # Opened the file in notepad++ and got the info of the data, hence slightly "hardcoded"
    cargo_stacks = defaultdict(deque)

    # [AMOUNT, FROM, TO]
    instructions = np.zeros((501, 3), dtype=int)
    for row_idx, line in enumerate(fid):
        if row_idx < 8:
            # Remove brackets and replace empty space with a dash
            crate_row = line.replace('[', '').replace(']', '').replace('    ', ' -').split()

            # Start 1 due to the instructions are between 1 and 9
            for col_idx, crate in enumerate(crate_row, start=1):
                if crate != '-':
                    cargo_stacks[col_idx].append(crate)
        elif row_idx > 9:
            instructions[row_idx - 10, :] = re.findall(r'\d+', line)


# Make a deepcopy for part 2
cargo_stacks_2 = copy.deepcopy(cargo_stacks)

# Not the most effective way, but one could have sliced, reversed and added
for n_moves, from_stack, to_stack in instructions:
    for _ in range(n_moves):
        crate = cargo_stacks[from_stack].popleft()
        cargo_stacks[to_stack].appendleft(crate)


# Get the top crates in each stack and print out the answer
top_crates_1 = ""
for _, cargo_stack in sorted(cargo_stacks.items()):
    crate = cargo_stack.popleft()
    top_crates_1 += crate


# Part 2
for n_moves, from_stack, to_stack in instructions:
    # Can't slice deque, hence using list comprehension
    crate_stack = [cargo_stacks_2[from_stack].popleft() for _ in range(n_moves)]

    # Reverse the order
    for crate in reversed(crate_stack):
        cargo_stacks_2[to_stack].appendleft(crate)


top_crates_2 = ""
for _, cargo_stack in sorted(cargo_stacks_2.items()):
    crate = cargo_stack.popleft()
    top_crates_2 += crate


print(f"Part 1; Top crates: {top_crates_1}")
print(f"Part 2; Top crates: {top_crates_2}")

"""
# With "solely" list comprehension, for part 1 remove reversed()

for n_moves, from_stack, to_stack in instructions:
    [cargo_stacks_2[to_stack].appendleft(crate) for crate in
     reversed([cargo_stacks_2[from_stack].popleft() for _ in range(n_moves)])]

"""
