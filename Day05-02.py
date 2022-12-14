from helpers.problemrunner import run_problem
from collections import deque
import re

@run_problem
def run():
    with open("Day05.txt") as f:
        lines = list(filter(None, (line.rstrip() for line in f)))

    crate_lines = []
    move_lines = []
    number_of_stacks = 0
    for line in lines:
        # Replace an empty space in a stack by '[ ]'
        if line.lstrip().startswith('['):
            crate_lines.append(line.replace("    ", "[ ]"))
        if line.lstrip().startswith('1'):
            number_of_stacks = int(line.rstrip()[-1])
        if (line.startswith("move")):
            move_lines.append(line.lstrip("move "))

    stacks = [deque() for _ in range(number_of_stacks)]
    for crate_line in crate_lines:
        # Replace '[' by '~' as '[' is a control character in regex 
        crate_indices = [m.start() for m in re.finditer('~', crate_line.replace('[', '~'))]
        stack_index = 0
        for i in crate_indices:
            crate = crate_line[i + 1].strip()
            if len(crate) > 0:
                stacks[stack_index].append(crate_line[i + 1])
            stack_index += 1

    moves = []
    for move_line in move_lines:
        split1 = move_line.split(" from ")
        split2 = split1[1].split(" to ")
        moves.append(Move(int(split1[0]), int(split2[0]) - 1, int(split2[1]) - 1))

    storage = Storage(stacks)
    storage.apply_moves(moves)

    return ''.join([stack[0] for stack in storage.stacks])


class Storage:
    def __init__(self, stacks):
        self.stacks = stacks

    def apply_moves(self, moves):
        for move in moves:
            self.move(move.count, move.from_stack, move.to_stack)

    def move(self, count, from_stack, to_stack):
        # Appended items have to be reversed as they are inserted one by one from left to right
        self.stacks[to_stack].extendleft(list(self.stacks[from_stack])[:count][::-1])
        self.stacks[from_stack] = deque(list(self.stacks[from_stack])[count:])

class Move:
    def __init__(self, count, from_stack, to_stack):
        self.count = count
        self.from_stack = from_stack
        self.to_stack = to_stack


run()
