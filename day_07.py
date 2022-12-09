#!/usr/bin/env python
# @Author: Foad Alhayek (a448431)
# @Filename: day_07.py
# @Date: 2022-12-07
# @Description: My simple implementation of the Advent of Code daily challenge, the code is not to be considered 
#               optimized nor the best, but instead a fun first-hand implementation done rather quickly or experimenting
#               with Python. Some solutions are over the top due to me trying different ways to solve the task.
from collections import defaultdict

# Read in the input
with open("data/day_07.txt", "r", encoding="utf-8") as fid:
    terminal_commands = [line.split() for line in fid]

# Initialize directory path and size list
dir_path = []
dir_size = defaultdict(int)

# Structure the file system and compute each directory's size
for cmd_line in terminal_commands:
    # Intentionally ignore "dir" and "ls" as they are not needed for this implementation
    if cmd_line[1] == "cd":
        if cmd_line[2] == "..":
            dir_path.pop()
        else:
            dir_path.append(cmd_line[2])
    elif cmd_line[0].isdigit():
        file_size = int(cmd_line[0])

        # Add file size to current dir and all parents. Not the most effective way, but it works
        for i in range(1, len(dir_path) + 1):
            dir_size["/".join(dir_path[:i])] += file_size


# Part 1 initialize
sum_of_dir = 0

# Part 2 initialize
total_disk_space = 70000000
need_space_for_update = 30000000

# Compute allowed amount of used space and initialize size of free dir to max (will be minimized later)
allowed_used_space = total_disk_space - need_space_for_update
size_of_free_dir = total_disk_space

# Compute the amount of space we need to free up based on the size of the root directory
free_up_space = dir_size["/"] - allowed_used_space

# Solve part 1 and part 2
for key, size in dir_size.items():
    # Part 1, find all dir which total size is less than 100000
    if size <= 100000:
        sum_of_dir += size

    # Part 2, find the smallest sized dir to free up enough space for the update
    if free_up_space <= size <= size_of_free_dir:
        size_of_free_dir = size

print(f"Part 1; Total size of dir under size 100000: {sum_of_dir}")
print(f"Part 2; Removed directory with total size of: {size_of_free_dir}")
