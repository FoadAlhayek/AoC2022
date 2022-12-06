#!/usr/bin/env python
# @Author: Foad Alhayek (a448431)
# @Filename: day_03.py
# @Date: 2022-12-05
# @Description: My simple implementation of the Advent of Code daily challenge, the code is not to be considered 
#               optimized nor the best, but instead a fun first-hand implementation done rather quickly or experimenting
#               with Python. Some solutions are over the top due to me trying different ways to solve the task.

def priority_conversion(character):
    """
    Converts characters aA-zZ to "priority" value 1-52
    :param character: A char [aA-zZ]
    :return: priority value 1-52
    """""
    ascii_value = ord(character)
    priority_value = None

    if 97 <= ascii_value <= 122:            # a to z
        # According to task: priority 1 to 26
        priority_value = ascii_value - 96
    elif 65 <= ascii_value <= 90:           # A to Z
        # According to task: priority 27 to 52
        priority_value = ascii_value - 38

    return priority_value


# We sum up duplicate values - task calls them "priority"
priority_1 = 0
priority_2 = 0

with open("data/day_03.txt", "r", encoding="utf-8") as fid:
    for n_third_idx, line in enumerate(fid, start=1):
        line = line.replace('\n', '')
        # Divide the string into "two compartments"
        idx = int(len(line)/2)

        # Sufficient to only look at unique letters
        compartment_one = set(line[:idx])
        compartment_two = set(line[idx:])

        # Part 1
        for letter in compartment_two:
            if letter in compartment_one:
                p_value = priority_conversion(letter)
                priority_1 += p_value

                # Should only be 1 "item" which is duplicate, so no need to loop more than necessary
                break

        # Part 2 - group of 3
        # Find the common letter between the three elves
        if n_third_idx % 3 == 1:
            elf_one = set(line)
        elif n_third_idx % 3 == 2:
            elf_two = set(line)
        elif n_third_idx % 3 == 0:
            elf_three = set(line)
            for letter in elf_three:
                if letter in elf_one and letter in elf_two:
                    p_value = priority_conversion(letter)
                    priority_2 += p_value

                    # Once found, break the loop
                    break


print(f"Part 1; Sum of priorities: {priority_1}")
print(f"Part 2; Sum of priorities: {priority_2}")
