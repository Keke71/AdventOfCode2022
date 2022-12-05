from helpers.problemrunner import run_problem

values = {"X": 1, "Y": 2, "Z": 3}

@run_problem
def run():
    with open("Day02.txt") as f:
        scores = [get_score(line.rstrip()) for line in f]

    return sum(scores)

def get_score(move):
    return values[move[2]] + get_result_Score(move)

def get_result_Score(move):
    return 3 if is_draw(move) else 6 if is_win(move) else 0

def is_draw(move):
    return move[0] == "A" and move[2] == "X" or move[0] == "B" and move[2] == "Y" or move[0] == "C" and move[2] == "Z"

def is_win(move):
    return move[0] == "A" and move[2] == "Y" or move[0] == "B" and move[2] == "Z" or move[0] == "C" and move[2] == "X"

run()
