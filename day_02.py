#!/usr/bin/env python
# @Author: Foad Alhayek (a448431)
# @Filename: day_02.py
# @Date: 2022-12-02
# @Description: My simple implementation of the Advent of Code daily challenge, the code is not to be considered 
#               optimized nor the best, but instead a fun first-hand implementation done rather quickly or experimenting
#               with Python. Some solutions are over the top due to me trying different ways to solve the task.
from enum import Enum


class GameStrLogic(Enum):
    """
    The logic based on the task description.
    O = Our; T = Their; print output will be default rock, paper, and scissor name
    """
    # Their/Opponent
    ROCK_T = "A"
    PAPER_T = "B"
    SCISSORS_T = "C"

    # Our/Player
    ROCK_O = "X"
    PAPER_O = "Y"
    SCISSORS_O = "Z"

    # Score logic
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name.split("_")[0]

    def get_value(self):
        material = self.name.split("_")[0]
        return GameStrLogic[material].value


def game_logic(our, their):
    """
    Loss = 0, Draw = 1, Win = 2 (used to multiply with score 3)
    :param our: rock, paper, scissor [String]
    :param their: rock, paper, scissor [String]
    :return: outcome [int]
    """
    # Rock, Paper, Scissors
    rock = GameStrLogic.ROCK.name
    paper = GameStrLogic.PAPER.name
    scissors = GameStrLogic.SCISSORS.name

    # Enemy logic, ex if they choose Paper (paper_logic) we win if we choose Scissors (index 2)
    rock_logic = [1, 2, 0]
    paper_logic = [0, 1, 2]
    scissors_logic = [2, 0, 1]
    str_logic = [rock, paper, scissors]

    # Return the outcome of the match
    our_idx = str_logic.index(our)
    if their == rock:
        return rock_logic[our_idx]
    elif their == paper:
        return paper_logic[our_idx]
    elif their == scissors:
        return scissors_logic[our_idx]
    else:
        print(f"Something went wrong in game_logic!\nour: {our}\ntheir: {their}")
        return None


def round_logic(round_outcome, their):
    """
    X means we need to lose
    Y means we need to draw
    Z means we need to won

    :param round_outcome: chr [X, Y or Z]
    :param their: Rock, Paper, Scissors
    :return: Our choice to match the outcome
    """
    if round_outcome == "X":
        outcome_logic = 0
    elif round_outcome == "Y":
        outcome_logic = 1
    elif round_outcome == "Z":
        outcome_logic = 2
    else:
        outcome_logic = None

    # Rock, Paper, Scissors
    rock = GameStrLogic.ROCK.name
    paper = GameStrLogic.PAPER.name
    scissors = GameStrLogic.SCISSORS.name

    # Enemy logic, ex if they choose Paper (paper_logic) we win if we choose Scissors (index 2)
    rock_logic = [1, 2, 0]
    paper_logic = [0, 1, 2]
    scissors_logic = [2, 0, 1]
    str_logic = [rock, paper, scissors]

    if their == rock:
        return str_logic[rock_logic.index(outcome_logic)]
    elif their == paper:
        return str_logic[paper_logic.index(outcome_logic)]
    elif their == scissors:
        return str_logic[scissors_logic.index(outcome_logic)]
    else:
        print(f"Something went wrong in round_logic!")
        return None


with open("data/day_02.txt", "r", encoding="utf-8") as fid:
    total_score = 0
    total_score_part2 = 0
    base_score = 3

    for line in fid:
        their_chr, our_chr = line.split()
        their_choice = str(GameStrLogic(their_chr))
        our_choice = str(GameStrLogic(our_chr))

        # Loss = 0, Draw = 1, Win = 2
        outcome = game_logic(our_choice, their_choice)

        # Scoring according to the task description
        total_score += outcome*base_score + GameStrLogic(our_chr).get_value()

        # Part 2 - X means we need to lose, Y means we need to draw, Z means we need to wom
        our_choice_part2 = round_logic(our_chr, their_choice)
        outcome_part_2 = game_logic(our_choice_part2, their_choice)
        total_score_part2 += outcome_part_2*base_score + GameStrLogic[our_choice_part2].get_value()

print(f"Part 1, Total score: {total_score}")
print(f"Part 2, Total score: {total_score_part2}")
