#!/usr/bin/env python
# @Author: Foad Alhayek (a448431)
# @Filename: day_06.py
# @Date: 2022-12-06
# @Description: My simple implementation of the Advent of Code daily challenge, the code is not to be considered 
#               optimized nor the best, but instead a fun first-hand implementation done rather quickly or experimenting
#               with Python. Some solutions are over the top due to me trying different ways to solve the task.

def chunk_generator(seq, size: int):
    """
    Create a generator which reads in N at the time
    :param seq: A string
    :param size: N
    :return:
    """
    return (seq[pos:(pos + size)] for pos in range(0, len(seq)))


def find_start_marker(msg_string, size):
    """
    Create and use a generator to find first N sized unique sequence and return the amount of characters processed
    before first unique sequence is detected.
    :param msg_string: String
    :param size: N integer
    :return: Integer
    """
    gen_char = chunk_generator(msg_string, size)

    # Start "size" because generator reads in "size" characters at the start
    for idx, char in enumerate(gen_char, start=size):
        if len(set(char)) == size:
            return idx

    return None


with open("data/day_06.txt", "r", encoding="utf-8") as fid:
    data_str = fid.readline()


# Compute part 1: 4 and part 2: 14
start_packet_marker = find_start_marker(data_str, 4)
start_msg_marker = find_start_marker(data_str, 14)

print(f"Part 1; Start-of-paket marker detected after {start_packet_marker} characters!")
print(f"Part 2; Start-of-message marker detected after {start_msg_marker} characters!")
